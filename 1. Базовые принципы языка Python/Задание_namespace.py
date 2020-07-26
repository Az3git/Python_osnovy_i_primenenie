General_globals = {'global': {}}
summ = "@"
listtop = []
from itertools import groupby

n = int(input())



def create_method (new_space, available_space, current_dict = General_globals):
    search = current_dict.get(available_space)
    if search is not None:
        search.update({new_space: {}})
        return 1
    else:
        for keys in current_dict:
            if type(current_dict.get(keys)) == dict:
                search_local = current_dict.get(keys).get(available_space)
                if search_local is not None:
                    search_local.update({new_space: {}})
                    return 1

                else:
                    create_method(new_space, available_space, current_dict.get(keys))

def add_method (available_space, plaggable, current_dict = General_globals):
    search = current_dict.get(available_space)
    if search is not None:
        search[plaggable+summ] = plaggable
        return 1
    else:
        for keys in current_dict:
            if type(current_dict.get(keys)) == dict:
                search_local = current_dict.get(keys).get(available_space)
                if search_local is not None:
                    search_local[plaggable+summ] = plaggable
                    return 1

                else:
                    add_method(available_space, plaggable, current_dict.get(keys))

def get_method (start_space, search_variable, current_dict = General_globals):
    global listtop


    search = current_dict.get(start_space)

    if search is not None:
        for elemt in search:
            if type(elemt) == str and elemt == search_variable:
                return start_space

    else:
        for keys in current_dict:

            if type(current_dict.get(keys)) == dict:

                search_local = current_dict.get(keys).get(start_space)

                if search_local is not None:
                    listtop.append(keys)
                    for elen in search_local:
                        if type(elen) == str and elen == search_variable:

                            return start_space
                    return listtop

                else:
                    listtop.append(keys)
                    resu = get_method(start_space, search_variable, current_dict.get(keys))
                    if resu is not None:
                        return resu

        del listtop[-1]
    return None


def search_value(listens, peremen):
    namescope = ''
    search_locals = General_globals.copy()
    for elema in listens:
        search_locals = search_locals.get(elema)
        for eov in search_locals:
            if type(eov) == str and eov == peremen:
                namescope = elema
    if namescope == '':
        return None
    else:
        return namescope




for i in range(n):
    command, argum_one, argum_two = map(str, input().split())

    if command == 'create':
        create_method(argum_one, argum_two)


    if command == 'add':
        add_method(argum_one, argum_two)


    if command == 'get':
        kekw = get_method(argum_one, argum_two+summ)

        if type(kekw) != list:
            print(kekw)
        else:
            print(search_value(kekw, argum_two + summ))

        listtop.clear()