General_globals = {'global': {}}
space_input = ''
get_res = ''


n = int(input())



def create_method (new_space, available_space, current_dict = General_globals):
    boole = False
    for el in current_dict:
        if type(current_dict.get(el)) == dict:
            boole = True

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
        search.update({plaggable: plaggable})
        return 1
    else:
        for keys in current_dict:
            if type(current_dict.get(keys)) == dict:
                search_local = current_dict.get(keys).get(available_space)
                if search_local is not None:
                    search_local.update({plaggable: plaggable})
                    return 1

                else:
                    add_method(available_space, plaggable, current_dict.get(keys))

def get_method (start_space, search_variable, current_dict = General_globals, current_dict_name = 'General_globals'):
    global space_input
    global get_res


    search = current_dict.get(start_space)

    if search is not None:
        for elemt in search:
            if type(elemt) == str and elemt == search_variable:
                get_res = start_space
                return start_space

    else:
        for keys in current_dict:
            if type(keys) == str and keys == search_variable:
                    space_input = current_dict_name

            if type(current_dict.get(keys)) == dict:
                for keyc in current_dict.get(keys):
                    if type(keyc) == str and keyc == search_variable:
                        space_input = keys
                search_local = current_dict.get(keys).get(start_space)

                if search_local is not None:

                    for elemt in search_local:
                        if type(elemt) == str and elemt == search_variable:

                            get_res = start_space
                            return start_space

                else:

                    get_method(start_space, search_variable, current_dict.get(keys), keys)


    if space_input == '':
        return None
    else:
        return space_input




for i in range(n):
    command, argum_one, argum_two = map(str, input().split())

    if command == 'create':
        create_method(argum_one, argum_two)

    if command == 'add':
        add_method(argum_one, argum_two)

    if command == 'get':
        kekw = get_method(argum_one, argum_two)
        if get_res == '':
            print(kekw)
        else:
            print(get_res)
        get_res = ''
        space_input = ''


