from email_platform import db, ma

class Template(db.Model):
    __tablename__ = 'template'
    template_pk = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(1024))
