from flask import render_template, jsonify, request
from email_platform import app, contacts, users, groups

from email_platform.model import contact

"""
contacts = [
        { 'firstname': 'Jan', 'lastname': 'Kowalski', 'emailaddress':
            'jan.kowalski@home.pl', 'group_fk': '0' },
        { 'firstname': 'Adam', 'lastname': 'Nowak', 'emailaddress':
            'adam.nowak@home.pl', 'group_fk': '0' },
]
"""

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
    #return contacts.get_contacts()
    cs = contacts.get_contacts()
    return render_template('contacts.html', title="Contacts", contacts=cs)

@app.route("/contact/<int:contact_pk>")
def get_contact(contact_pk):
    return jsonify(contacts.get_contact(contact_pk))

"""
@app.route('/contacts', methods=['POST'])
def add_contact():
    contacts.append(request.get_json())
    return '', 204
"""

@app.route("/contact", methods=['POST'])
def add_contact():
    #print("hello contact POST data {0}".format(request.get_json()))
    print("hello contact POST")
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
    gas = groups.group_list.get_json_formatted_list()
    return render_template('groups.html', groups=gas)
