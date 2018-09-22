from settings.api import get_setting
import requests


def get_auth_payload():
    return {
        'user': get_setting('fse_user'),
        'password': get_setting('fse_password'),
        'offset': get_setting('fse_offset'),
        'event': get_setting('fse_login_event')
    }


def get_auth_session():
    url = get_setting('fse_userctl_url')
    session = requests.Session()
    session.post(url, data=get_auth_payload())
    return session
