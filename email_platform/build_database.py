import os
from email_platform import db
from email_platform.model.contact import Contact

contacts = [
        { 'firstname': 'Jan', 'lastname': 'Kowalski', 'emailaddress':
            'jan.kowalski@home.pl', 'group_id': '0' },
        { 'firstname': 'Adam', 'lastname': 'Nowak', 'emailaddress':
            'adam.nowak@home.pl', 'group_id': '0' },
]

if os.path.exists('contacts.db'):
    os.remove('contacts.db')

db.create_all()

for contact in contacts:
    c = Contact(firstname=contact['firstname'], lastname=contact['lastname'],
            emailaddress=contact['emailaddress'], group_id=contact['group_id'])
    db.session.add(c)

db.session.commit()
