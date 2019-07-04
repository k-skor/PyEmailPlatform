from email_platform import mail
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
    #user = "recruitment@flypsdm.io"
    #passwd = "surge-is-recruiting-2019"

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
    return request_codes
    #msg_sender = None
    #if account.emailaddress:
    #    msg_sender = (account.emailfromname, account.emailfromaddress)
    #else:
    #    msg_sender = account.emailfromaddress
    #msg_recipients = [c.emailaddress for c in group.contacts_list]
    #if len(msg_recipients) > 0 and msg_subject:
    #    msg = Message(body=msg_body,
    #            subject=msg_subject,
    #            sender=msg_sender,
    #            receipients=msg_recipients)
    #    mail.send(msg)

