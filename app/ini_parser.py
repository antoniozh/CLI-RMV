# ------------------------------------------------------------------------------

from os import path
import configparser

# ------------------------------------------------------------------------------


ini_path = path.join(path.dirname(path.realpath(__file__)), 'connections.ini')


def get_connection(name):
    cnf = configparser.ConfigParser()
    cnf.read(ini_path)
    if(name not in cnf.sections()):
        raise Exception("{0} not found in connections.ini".format(name))
    conn = cnf[name]
    try:
        origin = conn['origin']
        dest = conn['destination']
        return origin, dest
    except KeyError:
        print("origin or destination not found in {0} in connections.ini".format(name))
