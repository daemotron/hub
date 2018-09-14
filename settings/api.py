from .models import Setting


def create_or_update_setting(key, value):
    try:
        s = Setting.objects.get(key__exact=key)
    except Setting.DoesNotExist:
        s = Setting(key=key, value=b'')
        s.save()
    s.set(value)


def get_setting(key):
    try:
        s = Setting.objects.get(key__exact=key)
        return s.get()
    except Setting.DoesNotExist:
        return None
