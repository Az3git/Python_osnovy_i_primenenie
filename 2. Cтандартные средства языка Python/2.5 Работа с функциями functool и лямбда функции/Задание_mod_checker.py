from functools import partial

def ostatok(a, osstat, b):
    return b % a == osstat

def mod_checker(x, mod = 0): #x = 3, mod = 1
    return partial(ostatok, x, mod)
