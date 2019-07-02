from flask import make_response, abort
from email_platform import db
from email_platform.model import contact
from .groups import add_contact_to_group, change_contact_group

def get_contacts():
    cs = contact.Contact.query.order_by(contact.Contact.contact_pk).all()

    contact_schema = contact.ContactSchema(many=True)
    data = contact_schema.dump(cs).data
    print('---===---\n{0}\n---===---'.format(data))
    return data

#def get_contacts_for_group(group_id):
#    cs = contact.Contact.query.where(contact.Contact.group_id == group_id).order_by(contact.Contact.contact_pk).all()
#
#    contact_schema = contact.ContactSchema(many=True)
#    data = contact_schema.dump(cs).data
#    print('---===---\n{0}\n---===---'.format(data))
#    return data

def get_contact(contact_pk):
    c = contact.Contact.query.filter(contact.Contact.contact_pk ==
            contact_pk).one_or_none()

    if c is not None:
        contact_schema = contact.ContactSchema()
        data = contact_schema.dump(c).data
        return data
    else:
        abort(404, 'Contact not found for pk: \
        {contact_pk}'.format(contact_pk=contact_pk))

def create_contact(c):
    #cpk = c.get('contact_pk')
    print("hello create_contact")
    firstname = c.get('firstname')
    lname = c.get('lastname')
    emailaddr = c.get('emailaddress')
    gid = c.get('group_id')

    print('---===---\n{0}\n---===---'.format(c))
    existing_contact = (
            contact.Contact.query.filter(contact.Contact.emailaddress ==
                emailaddr).one_or_none()
    )

    if existing_contact is None:
        schema = contact.ContactSchema()
        new_contact = schema.load(c, session=db.session).data
        add_contact_to_group(new_contact)
        print(new_contact)

        for obj in db.session:
            print(obj)
        db.session.add(new_contact)
        db.session.commit()

        return schema.dump(new_contact).data, 201

    else:
        abort(409, 'Contact {fname} {lname} {emailaddr} exists \
                already'.format(fname=fname, lname=lname, emailaddr=emailaddr))

def update_contact(contact_pk, c):
    update_contact = contact.Contact.query.filter(contact.Contact.contact_pk ==
            contact_pk).one_or_none()

    firstname = c.get('firstname')
    lname = c.get('lastname')
    emailaddr = c.get('emailaddress')
    gid = c.get('group_id')

    existing_contact = (
            contact.Contact.query.filter(contact.Contact.emailaddress ==
                emailaddr).one_or_none()
    )

    if update_contact is None:
            abort(404, 'Contact not found for pk: \
            {contact_pk}'.format(contact_pk=contact_pk))
    elif (
            existing_contact is not None and existing_contact.contact_pk !=
            contact_pk
    ):
            abort(409, 'Contact {fname} {lname} {emailaddr} exists \
                    already'.format(fname=fname, lname=lname, emailaddr=emailaddr))

    else:
            old_gid = update_contact.group_id
            schema = contact.ContactSchema()
            update = schema.load(c, session=db.session).data

            update.contact_pk = update_contact.contact_pk

            print("handle contact gr change, old {0} -> new \
                    {1}".format(old_gid, update.group_id))
            if old_gid != update.group_id:
                change_contact_group(update, old_gid)

            db.session.merge(update)
            db.session.commit()

            data = schema.dump(update_contact).data
            return data, 200

def delete_contact(contact_pk):
    contact = contact.Contact.query.filter(contact.Contact.contact_pk == contact_pk).one_or_none()

    if contact is not None:
        db.session.delete(contact)
        db.session.commit()
        return make_response('Contact {contact_pk} \
        delted'.format(contact_pk=contact_pk), 200)

    else:
        abort(404, "Contact not found for pk: \
        {contact_pk}".format(contact_pk=contact_pk))

