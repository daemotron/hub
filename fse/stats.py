import re
from xml.etree.ElementTree import fromstring

import requests
from xmljson import parker

from settings.api import get_setting


def get_stat(key):
    url = get_setting('fse_datafeed_stat')
    url = url.format(key, key)
    response = requests.get(url)
    if "Currently Closed for Maintenance" in response.text:
        raise RuntimeError('FSEconomy is currently down for maintenance. Please try again later.')
    clean = re.sub(r'<StatisticItems[^>]+>', '<StatisticItems>', response.text)
    data = parker.data(fromstring(clean))
    return data['Statistic']
