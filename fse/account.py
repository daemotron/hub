import requests


def get_account(username, type='1'):
    data = {'startsWith': username, 'accountType': type}
    server_error = 'Could not retrieve status information from FSEconomy.'
    server_error += ' If the error persists, please contact the Stormrose Team.'
    response = requests.post('http://server.fseconomy.net/namelookup.jsp', data=data)
    if "Currently Closed for Maintenance" in response.text:
        raise RuntimeError('FSEconomy is currently down for maintenance. Please try again later.')
    if response.status_code != 200:
        raise RuntimeError(server_error)
    if response.text.strip():
        return response.json()
    return {}


def get_account_id(username):
    data = get_account(username)
    try:
        account_id = data['accounts'][0]['value']
    except(IndexError, KeyError):
        account_id = 0
    return account_id
