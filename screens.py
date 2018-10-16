#!/usr/bin/env python
#-*- coding: utf-8 -*-

from functools import wraps


def menu(menu_text, options):
    while True:
        print(menu_text)
        option = input("Choose an option below: ")
        screen = options.get(option)
        if screen:
            if screen():
                break
        else:
            print("ERROR: INVALID OPTION!")

def modal(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('-' * 30)
        print(func.__name__)
        print('-' * 30)
        ret = func(*args, **kwargs)
        return ret
    return wrapper