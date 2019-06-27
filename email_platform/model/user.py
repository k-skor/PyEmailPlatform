from email_platform import db, ma
#from flask_marshmallow import fields
from marshmallow import Schema, fields, post_load

class User:
    def __init__(self, user_pk, accountlogin, accountpass, emailfromname,
            emailfromaddress):
        self.user_pk = user_pk
        self.accountlogin = accountlogin
        self.accountpass = accountpass
        self.emailfromname = emailfromname
        self.emailfromaddress = emailfromaddress
        #emailtemplate = db.Column(db.String(1024))
        #emailtemplate_fk = db.Column(db.Integer)

#    def __getitem__(self, key):
#        return self.user_pk
    def __repr__(self):
        return '<User(user_pk={self.user_pk!r})>'.format(self=self)

#class UserSchema(ma.ModelSchema):
#    class Meta:
#        model = User
#        sqla_session = db.session

class UserSchema(Schema):
    user_pk = fields.Integer()
    accountlogin = fields.String()
    accountpass = fields.String()
    emailfromname = fields.String()
    emailfromaddress = fields.String()

    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)

class UsersList:
    users = [
            User(0, "admin", "1234", "K. Skor", "ks0000@home.pl")
    ]

    def find_user(self, user_pk):
        for u in self.users:
            print('iterating user: {}'.format(u))
            if u.user_pk == user_pk:
                print('found for pk={pk}'.format(pk=user_pk))
                return u
        return None

    def remove_user(self, user):
        self.users.remove(user)

    def add_user(self, user):
        self.users.append(user);
