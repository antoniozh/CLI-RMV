# ------------------------------------------------------------------------------

import re
from bs4 import BeautifulSoup
import requests
import web_request

# ------------------------------------------------------------------------------


def get_origin_dest(html):
    res = []
    try:
        res = html.find('td', {'class': 'station'})
    except:
        print("Error during get_origin_dest")
    if(len(res) != 2):
        raise Exception("Too few or to many td's found in get_origin_dest")
    origin, dest = res
    return origin.text.strip(), dest.text.strip()


def get_time(html):
    res = []
    try:
        res = html.find('td', {'class': 'time'}).find('div', {'class': 'planed'})
    except:
        print("Error during get_time")
    if(len(res) is None):
        raise Exception("Too few or to many td's found in get_time")
    time = res.text.strip()
    try:
        dep, arr = time.split('\n')
    except:
        print("Error trying to split time string into depature and arrival")
    dep = dep.replace(' ab', '')
    arr = arr.replace(' an', '')
    return dep.strip(), arr.strip()


def get_duration(html):
    res = []
    try:
        res = html.find('td', {'class': 'duration'})
    except:
        print("Error during get_duration")
    if(len(res) != 1):
        raise Exception("Too few or to many td's found in get_duration")
    duration = res.text.strip()
    return duration


def get_transportation(html):
    res = []
    try:
        res = html.find('td', {'class': 'products'})
    except:
        print("Error during get_transportation")
    trans = []
    for product in res.findAll('img'):
        try:
            title = product.get('title')
        except:
            print("Error getting a title in get_transportation")
            print(product.text)
        trans.append(title)
    return trans


def get_html(origin, dest, time, da):
    html = web_request.get_html(origin, dest, time, da)
    return html


def get_plan(origin, dest, time, da):
    html = get_html(origin, dest, time, da)
    html = BeautifulSoup(html, 'html.parser')
    plan = []
    for tr in html.findAll('tr', {'id': re.compile('trOverviewC0-*')}):
        connection = {}
        origin, dest = get_origin_dest(tr)
        connection['origin'] = origin
        connection['dest'] = dest
        dep, arr = get_time(tr)
        connection['dep'] = dep
        connection['arr'] = arr
        duration = get_duration(tr)
        connection['duration'] = duration
        trans = get_transportation(tr)
        connection['trans'] = trans
        plan.append(connection)
    return plan
