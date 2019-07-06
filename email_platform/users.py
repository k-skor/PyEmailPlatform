from email_platform import db
from email_platform.model import user

user_list = user.UsersList()

def get_user(user_pk):
    account = user_list.find_account(user_pk)
    u = account[user.UsersList.USER_KEY]

    user_schema = user.UserSchema(strict=True)
    data, errors = user_schema.dump(u)
    print('---===---\nget\n{0}\nerrors:{1}\n---===---'.format(data, errors))
    return data

def update_user(user_pk, u):
    account = user_list.find_account(user_pk)
    update_user = account[user.UsersList.USER_KEY]

    login = u.get('accountlogin')
    password = u.get('accountpassword')
    emailfromname = u.get('emailname')
    emailfromaddress = u.get('emailaddress')

    if update_user is None:
            abort(404, 'User not found for pk: \
            {user_pk}'.format(user_pk=user_pk))

    else:
            schema = user.UserSchema()
            new_user = schema.load(u).data

            print(new_user)
            user_list.replace_user(update_user, new_user)

            data = schema.dump(new_user).data
            return data, 200
