from email_platform.model import group, user
#from flask_mail import Message

import requests, json

from .users import user_list
from .groups import group_list

def send_email():
    account = user_list.find_account(0)
    print(account)
    accountuser = account[user.UsersList.USER_KEY]
    emailmsg = account[user.UsersList.EMAIL_MSG_KEY]
    emailgroup = group_list.get_group(emailmsg.recipient_group_id)

    url = "https://api.flypsdm.io/public/api/v1/sendmail"

    payload = {
            'from': {
                'name': accountuser.emailfromname,
                'email': accountuser.emailfromaddress
            },
            'subject': emailmsg.subject,
            'text': emailmsg.body
    }
    headers = {
            'content-type': 'application/json'
    }
    request_codes = []
    for (i, c) in enumerate(emailgroup.contacts_list):
        payload['to'] = {
                'name': c.firstname + " " + c.lastname,
                'email': c.emailaddress
        }
        try:
            r = requests.post(
                    url,
                    data=json.dumps(payload),
                    headers=headers,
                    auth=requests.auth.HTTPBasicAuth(
                        accountuser.accountlogin,
                        accountuser.accountpass
                )
            )
            request_codes.append((c.emailaddress, r.status_code))
        except:
            request_codes.append((c.emailaddress, 0))
    return request_codes

