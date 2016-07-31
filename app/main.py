#! /usr/bin/python3

import re
import json
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
from datetime import datetime, time
from urllib import parse

headers = {'content-type': 'application/x-www-form-urlencoded'}
url = 'http://www.rmv.de/auskunft/bin/jp/query.exe/dn?OK#focus'


def pprint(connections):
    print("------------------------------------------------\n")
    for conn in connections:
        print("from:\t{0}".format(conn['origin']))
        print("to:\t{0}".format(conn['dest']))
        print('\n')
        print("dep.:\t{0}".format(conn['dep']))
        print("arr.:\t{0}".format(conn['arr']))
        print("dur.:\t{0}".format(conn['duration']))
        print('\n')
        print("trans.:\t{0}".format(', '.join(conn['trans'])))
        print("\n------------------------------------------------\n")


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
    if(len(res) == None):
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


def get_plan(soup):
    connections = []
    for tr in soup.findAll('tr', {'id': re.compile('trOverviewC0-*')}):
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
        connections.append(connection)
    pprint(connections)


if __name__ == '__main__':
    data = {'start': 1, 'isUserTime': 'yes', 'timesel': 'depart'}
    s = "Dieburg+Hochschule+S%C3%BCd"
    # data['S'] = parse.quote(s)
    data['S'] = s
    z = "Darmstadt+Schlo%C3%9F"
    # data['Z'] = parse.quote(z)
    data['Z'] = z
    t = time.strftime(datetime.now().time(), "%H:%M")
    data['time'] = parse.quote(t)
    res = requests.post(url, data=data)
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    get_plan(soup)
