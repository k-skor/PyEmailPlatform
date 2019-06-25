from flask_wtf import Form
from wtforms import StringField, PasswordField

class AccountSettingsForm(Form):
    accountlogin = StringField('Login')
    accountpass = PasswordField('Password')
