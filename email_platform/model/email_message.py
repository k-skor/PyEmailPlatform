from marshmallow import Schema, fields, post_load

class EmailMessage:
    def __init__(self, subject, body, recipient_group_id):
        self.subject = subject
        self.body = body
        self.recipient_group_id = recipient_group_id

    def clear(self):
        self.subject = ""
        sefl.body = ""
        self.recipient_group_id = 0

    def __repr__(self):
        return '<EmailMessage(recipient_group_id={self.recipient_group_id!r})>'.format(self=self)

class EmailMessageSchema(Schema):
    subject = fields.String(32)
    body = fields.String(1024)
    recipient_group_id = fields.Integer()

    @post_load
    def make_email_message(self, data, **kwargs):
        return EmailMessage(**data)
