from email_platform import db
from email_platform.model import user

user_list = user.UsersList()

def get_user(user_pk):
    #u = user.User.query.order_by(user.User.user_pk).all()
    u = user_list.find_user(user_pk)

    #print('found user {id} {login} {passwd} {emailname} ' \
    #        '{emailaddress}'.format(id=u.user_pk, login=u.accountlogin,
    #            passwd=u.accountpass, emailname=u.emailfromname,
    #            emailaddress=u.emailfromaddress))
    user_schema = user.UserSchema(strict=True)
    data, errors = user_schema.dump(u)
    print('---===---\nget\n{0}\nerrors:{1}\n---===---'.format(data, errors))
    return data

def update_user(user_pk, u):
    #update_user = user.User.query.filter(user.User.user_pk ==
    #        user_pk).one_or_none()
    update_user = user_list.find_user(user_pk)

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
            #print('---===---\nput\n{0}\nerrors: {1}---===---'.format(new_user,
            #    errors))

            #print('found user {idx} {login} {passwd} {emailname} ' \
            #        '{emailaddress}'.format(idx=new_user.user_pk,
            #            login=new_user.accountlogin,
            #            passwd=new_user.accountpass, emailname=new_user.emailfromname,
            #            emailaddress=new_user.emailfromaddress))
            print(new_user)
            user_list.remove_user(update_user)
            user_list.add_user(new_user)

            data = schema.dump(new_user).data
            return data, 200
