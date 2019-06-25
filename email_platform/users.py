from email_platform import db
from email_platform.model import user

def get_user(user_pk):
    u = user.User.query.order_by(user.User.user_pk).all()

    user_schema = user.UserSchema(many=True)
    data = user_schema.dump(u).data
    print('---===---\n{0}\n---===---'.format(data))
    return data

def update_user(user_pk, u):
    update_user = user.User.query.filter(user.User.user_pk ==
            user_pk).one_or_none()

    login = u.get('accountlogin')
    password = u.get('accountpassword')
    emailfromname = u.get('emailname')
    emailfromaddress = u.get('emailaddress')

    if update_user is None:
            abort(404, 'User not found for pk: \
            {user_pk}'.format(user_pk=user_pk))

    else:
            schema = user.UserSchema()
            update = schema.load(u, session=db.session).data

            update.user_pk = update_user.user_pk

            db.session.merge(update)
            db.session.commit()

            data = schema.dump(update_user).data
            return data, 200
