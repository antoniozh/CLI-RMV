#! /usr/bin/python3
# ------------------------------------------------------------------------------

from datetime import datetime, time
from urllib import parse
import argparse
from argparse import RawTextHelpFormatter
import re

import parser
import ini_parser
import pprint

# ------------------------------------------------------------------------------


arg_parser = argparse.ArgumentParser(description='command-line app for parser connections', formatter_class=RawTextHelpFormatter)
arg_parser.add_argument('-c', metavar='--connection', type=str, help='connection defined in [..] in connections.ini')
arg_parser.add_argument('-d', metavar='--departure', type=str, help='time of departe (HH:MM)\nExample: -d 12:00')
arg_parser.add_argument('-a', metavar='--arrival', type=str, help='time of arrival (HH:MM)\nExample: -a 14:00')
arg_parser.add_argument('-D', metavar='--destination', type=str, help='destination station (must match RMV)\nExample: -D "Darmstadt Schloß""')
arg_parser.add_argument('-O', metavar='--origin', type=str, help='origin station (must match RMV)\nExample: -O "Darmstadt Hauptbahnhof"')
args = arg_parser.parse_args()


def get_time(t):
    if(re.search(r"([0-1]*[0-9]|2[0-3]):[0-5][0-9]", t) is None):
        raise Exception("time needs to be HH:MM format")
    else:
        return t


def get_args():
    if(args.c is not None):
        origin, dest = ini_parser.get_connection(args.c)
    elif(args.D is None or args.O is None):
        raise Exception("origin/destination not set")
    else:
        origin, dest = args.O, args.D
    if(args.a is None and args.d is None):
        da = 'depart'
        t = time.strftime(datetime.now().time(), "%H:%M")
    elif(args.a is not None and args.d is not None):
        raise Exception("Depature/Arrival flag cannot be set at the same time")
    elif(args.d is not None):
        da = 'depart'
        t = get_time(args.d)
    else:
        da = 'arrive'
        t = get_time(args.a)
    return origin, dest, t, da


if __name__ == '__main__':
    try:
        origin, dest, time, da = get_args()
        plan = parser.get_plan(origin, dest, time, da)
        pprint.pprint(plan)
    except Exception as e:
        print("Error: " + str(e))
