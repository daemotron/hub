from settings.api import get_setting
from .account import get_account_id
from .auth import get_auth_session


def issue_payment(sender, receiver, amount, comment):
    url = get_setting('fse_userctl_url')
    payload = {
        'event': get_setting('fse_payment_event'),
        'id': get_account_id(sender),
        'account': get_account_id(receiver),
        'amount': str(amount),
        'comment': str(comment)
    }
    session = get_auth_session()
    response = session.post(url, data=payload)
    if "Currently Closed for Maintenance" in response.text:
        raise RuntimeError('FSEconomy is currently down for maintenance. Please try again later.')
    session.close()
