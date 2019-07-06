from datetime import datetime
from email_platform import db, ma
from marshmallow import fields

class Contact(db.Model):
    __tablename__ = 'contact'
    contact_pk = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(32))
    lastname = db.Column(db.String(32))
    emailaddress = db.Column(db.String(32))
    group_id = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow,
            onupdate=datetime.utcnow)

    def __eq__(self, other):
        return self.contact_pk == other.contact_pk

    def __repr__(self):
        return '<Contact(contact_pk={self.contact_pk!r})>'.format(self=self)

class ContactSchema(ma.ModelSchema):
    group_id = fields.Integer(missing=0)
    class Meta:
        model = Contact
        sqla_session = db.session
