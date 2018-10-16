#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys
from selection_sort import sel_sort
from insertion_sort import ins_sort
from screens import menu, modal


def open_file():

    with open('arquivoInicial.txt', 'r') as f:
        data = f.read()
    list_data = data.splitlines()
    final_list = []
    for row in list_data:
        temp_list = row.split(",")
        for i in temp_list:
            final_list.append(i)
    return final_list


@modal
def exit():
    print('Bye bye!')
    sys.exit(0)


def selection():
    data = open_file()
    sel_sort(data)
    print(data)


def insertion():
    data = open_file()
    ins_sort(data)
    print(data)


def back():
    return True


@modal
def enter():
    menu_text = """
    Menu:
        1 - Selection Sort
        2 - Insertion Sort
        3 - Back
    """
    options = {
        '1': selection,
        '2': insertion,
        # '3': heap,
        # '4': merge,
        '3': back,
    }
    menu(menu_text, options)


@modal
def home():
    menu_text = """
    Menu:
        1 - Show Sorting Methods
        9 - Exit
    """
    options = {
        '1': enter,
        '9': exit
    }
    menu(menu_text, options)


if __name__ == '__main__':
    try:
        home()
    except KeyboardInterrupt:
        exit()
