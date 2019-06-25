from email_platform import db, ma

class User(db.Model):
    __tablename__ = 'user'
    user_pk = db.Column(db.Integer, primary_key=True)
    accountlogin = db.Column(db.String(32))
    accountpass = db.Column(db.String(32))
    emailfromname = db.Column(db.String(32))
    emailfromaddress = db.Column(db.String(32))
    #emailtemplate = db.Column(db.String(1024))
    emailtemplate_fk = db.Column(db.Integer)

class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
        sqla_session = db.session
