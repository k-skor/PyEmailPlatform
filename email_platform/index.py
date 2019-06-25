from flask import render_template, jsonify, request
from email_platform import app, contacts, users

"""
contacts = [
        { 'firstname': 'Jan', 'lastname': 'Kowalski', 'emailaddress':
            'jan.kowalski@home.pl', 'group_fk': '0' },
        { 'firstname': 'Adam', 'lastname': 'Nowak', 'emailaddress':
            'adam.nowak@home.pl', 'group_fk': '0' },
]
"""

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

@app.route("/settings")
def get_settings():
    u = users.get_user(0)
    return render_template('settings.html', user=u)
