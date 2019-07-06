from flask import render_template, jsonify, request, abort
from email_platform import app, contacts, users, groups
from email_platform.email_service import send_email

from email_platform.model import contact, user, group, email_message

def init_groups():
    cs = contact.Contact.query.order_by(contact.Contact.contact_pk).all()
    for c in cs:
        g = groups.group_list.get_group(c.group_id)
        if g is not None:
            groups.add_contact_to_group(c)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/contacts")
def get_contacts():
    cs = contacts.get_contacts()
    return render_template('contacts.html', title="Contacts", contacts=cs)

@app.route("/contact/<int:contact_pk>")
def get_contact(contact_pk):
    return jsonify(contacts.get_contact(contact_pk))

@app.route("/contact", methods=['POST'])
def add_contact():
    print(request.form)
    contacts.create_contact(request.form)
    return '', 204

@app.route("/contact_edit/<int:contact_pk>")
def edit_contact(contact_pk):
    c = contacts.get_contact(contact_pk)
    return render_template('contact_edit.html', title="Edit contact", contact=c)

@app.route("/contact_edit/<int:contact_pk>", methods=['POST'])
def update_contact(contact_pk):
    print(request.form)
    contacts.update_contact(contact_pk, request.form)
    return '', 204

@app.route("/settings")
def get_settings():
    u = users.get_user(0)
    return render_template('settings.html', user=u)

@app.route("/settings", methods=['POST'])
def update_settings():
    print("hello user POST")
    print(request.form)
    users.update_user(0, request.form)
    return '', 204

@app.route("/groups")
def get_groups():
    gs = groups.group_list.get_groups()
    gs_schema = group.ContactGroupSchema()
    gs_data = gs_schema.dump(gs, many=True).data
    return render_template('groups.html', groups=gs_data)

@app.route("/email_send")
def get_send_email():
    gs = groups.group_list.get_groups()
    gs_schema = group.ContactGroupSchema()
    gs_data = gs_schema.dump(gs, many=True).data
    a = users.user_list.find_account(0)
    em_schema = email_message.EmailMessageSchema()
    em_data = em_schema.dump(a[user.UsersList.EMAIL_MSG_KEY]).data
    return render_template('email_template.html', email_msg=em_data,
            groups=gs_data)

@app.route("/email_send", methods=['POST'])
def email_send():
    print(request.form)
    em_schema = email_message.EmailMessageSchema()
    em = em_schema.load(request.form).data
    print("loaded email msg: {}".format(em))
    a = users.user_list.find_account(0)
    a[user.UsersList.EMAIL_MSG_KEY] = em
    codes = send_email()
    error_response = []
    for (email, code) in codes:
        if code != 202:
            print("result code {} for email {}".format(code, email))
            error_response.append(email)
    print("send with error msg:\n" + (" ".join(error_response)))
    if len(error_response) > 0:
        abort(400, "Failed to send email to \
                receipients:\n" + (" ".join(error_response)))
    return '', 204
