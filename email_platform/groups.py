from email_platform.model import group

group_list = group.ContactGroupList()

def add_contact_to_group(contact):
    g = group_list.get_group(contact.group_id)
    g.contacts_list.append(contact)

def change_contact_group(contact, group_id):
    old_group = group_list.get_group(group_id)
    print("remove contact id: {}".format(contact.contact_pk))
    if old_group is not None:
        print("contacts list: {}".format(old_group.contacts_list))
        old_group.contacts_list.remove(contact)

    print("change contact group, old {0} -> new {1}".format(old_group, group_id))
    add_contact_to_group(contact)
