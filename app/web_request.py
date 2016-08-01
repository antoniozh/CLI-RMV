# ------------------------------------------------------------------------------

import requests
import re

# ------------------------------------------------------------------------------


headers = {'content-type': 'application/x-www-form-urlencoded'}
url = 'http://www.rmv.de/auskunft/bin/jp/query.exe/dn?OK#focus'
data = {'start': 1, 'isUserTime': 'yes'}


def get_html(origin, dest, time, da='depart'):
    data['S'] = origin
    data['Z'] = dest
    data['time'] = time
    data['timesel'] = da
    try:
        res = requests.post(url, data=data)
    except:
        print('Error while during web request')
    if(res is None or res.text is None):
        raise Exception("parser Respone is None")
    html = res.text
    if(re.search(r"Ihre Verbindungsanfrage", html) is not None):
        raise Exception("Wrong origin/destination string")
    return html
