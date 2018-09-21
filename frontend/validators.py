from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from fse.account import get_account


def fse_username_validator(username):
    flag = True
    try:
        _ = User.objects.get(username=username)
    except User.DoesNotExist():
        flag = False
    if flag:
        raise ValidationError(
            '%(value)s is already registered. Double registration is not allowed.',
            params={'value': username}
        )
    try:
        data = get_account(username, type='2')
    except RuntimeError as err:
        raise ValidationError('{}'.format(err))
    try:
        value = data['accounts'][0]['label']
    except (KeyError, IndexError):
        raise ValidationError('%(value)s is not a valid FSEconomy account', params={'value': username})
    if value != username:
        raise ValidationError('%(value)s is not a valid FSEconomy account', params={'value': username})
