from flask import Flask, jsonify, request
app = Flask(__name__)

contacts = [
        { 'firstname': 'Jan', 'lastname': 'Kowalski', 'email':
            'jan.kowalski@home.pl', 'group_pk': '0' }
]

@app.route("/contacts")
def get_contacts():
    return jsonify(contacts)

@app.route('/contacts', methods=['POST'])
def add_contact():
    contacts.append(request.get_json())
    return '', 204
