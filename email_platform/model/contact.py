from datetime import datetime
from email_platform import db, ma

from .groups import ContactGroup

class Contact(db.Model):
    __tablename__ = 'contact'
    contact_pk = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(32))
    lastname = db.Column(db.String(32))
    emailaddress = db.Column(db.String(32))
    group_id = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow,
            onupdate=datetime.utcnow)

class ContactSchema(ma.ModelSchema):
    class Meta:
        model = Contact
        sqla_session = db.session
