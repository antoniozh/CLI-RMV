def pprint(connections):
    print("\n------------------------------------------------\n")
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
