import os
import time
import shlex
import struct
import platform
import subprocess

from zeep import Client
from lxml import etree
import subprocess as sp

client = Client('https://www.pttor.com/OilPrice.asmx?WSDL')
cal = ['', 'LITER -> MONEY', 'MONEY -> LITER']

sp.call('cls', shell=True)

sp.run('', shell=True)


def _get_terminal_size_windows():
    try:
        from ctypes import windll, create_string_buffer
        # stdin handle is -10
        # stdout handle is -11
        # stderr handle is -12
        h = windll.kernel32.GetStdHandle(-12)
        csbi = create_string_buffer(22)
        res = windll.kernel32.GetConsoleScreenBufferInfo(h, csbi)
        if res:
            (bufx, bufy, curx, cury, wattr,
             left, top, right, bottom,
             maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
            sizex = right - left + 1
            sizey = bottom - top + 1
            return sizex, sizey
    except:
        return 80, 24


def home(sizex, sizey):
    os.system('cls')
    row = sizey // 2 - 3
    col = sizex - 1
    print("*" * (col))
    for i in range(row):
        print("*" + ' ' * (col - 2) + '*')
    print('*' + ' ' * (col // 2 - 10) + "PETROL SALE SYSTEM", end='')
    print(' ' * (col - col // 2 - 10) + '*')
    print('*' + ' ' * (col // 2 - 12) + 'Author: Nhan Le Thi Thanh', end='')
    print(' ' * (col - col // 2 - 15) + '*')
    print('*' + ' ' * (col // 2 - 11) + 'Published at 09/01/2020', end='')
    print(' ' * (col - col // 2 - 14) + '*')
    print("*" + ' ' * (col - 2) + '*')
    print("*" + ' ' * (col - 2) + '*')
    print("*" + ' ' * (col - 2) + '*')
    print("*" + ' ' * (col // 2 - 20) + "WELCOME TO OUR SYSTEM!", end='')
    print(' PLEASE PRESS ANY KEY TO CONTINUE...\0337', end='')
    print(' ' * (col - col // 2 - 40) + "*")
    for i in range(row - 3):
        print("*" + ' ' * (col - 2) + '*')
    print("*" * (col) + '\0338', end='')


def update_price():
    result = client.service.CurrentOilPrice(Language="en")
    root = etree.fromstring(result)
    for i in range(len(root)):
        if len(root[i]) == 3:
            name.append(root[i][1].text)
            price.append(float(root[i][2].text))


def menu(sizex, sizey):
    os.system('cls')
    row = sizey // 2 - 1
    col = sizex - 1
    val = col // 2
    print("*" * (col))
    for i in range(0, row - len(name) // 2 - 1):
        print("*" + ' ' * (col - 2) + '*')
    print('*' + ' ' * (val - 2) + 'MENU' + ' ' * (col - val - 4) + '*')
    for i in range(1, len(name)):
        s = str(i) + '. ' + name[i] + ' : ' + str(price[i]) + ' BAHT'
        print('*' + (val - 10) * ' ' + s, end='')
        print((col - len(s) - val + 8) * ' ' + '*')
    for i in range(0, row - len(name) // 2):
        print("*" + ' ' * (col - 2) + '*')
    print("*" + ' ' * (val - 17), end='')
    print("Please choose the kind of petrol: \0337", end='')
    print(' ' * (col - val - 19) + "*" + "\n" + "*" * col + '\0338', end='')


def ask(x, y, set):
    os.system('cls')
    col = x - 1
    row = (y - len(set)) // 2 - 1
    print("*" * col)
    for i in range(row):
        print("*" + ' ' * (col - 2) + "*")
    val = len(set)
    for i in set:
        print("*" + ' ' * (col // 2 - len(i) // 2) + i, end='')
        print(' ' * (col - (col // 2 - len(i) // 2) - len(i) - 2) + "*")
    for i in range(row - 1):
        print("*" + ' ' * (col - 2) + "*")
    print("*" + ' ' * (col // 2 - 12), end='')
    print("Please enter the number: \0337", end='')
    print(' ' * (col - (col // 2) - 15) + "*\n", end='')
    print("*" * col + '\0338', end='')


if __name__ == '__main__':

    check = True
    while check:
        # Information about program
        os.system('cls')
        sizex, sizey = _get_terminal_size_windows()
        print(sizex, sizey)
        home(sizex, sizey)
        input()

        # Update data from website
        name = ['none']
        price = [0]
        update_price()
        # print out menu of petrol type and input oil type
        oil_type = n = k = m = c = ''
        while not (k.isnumeric() and int(k) in range(1, len(name))):
            menu(sizex, sizey)
            k = input()
        k = int(k)

        set = [str(name[k]) + ' - price : ' + str(price[k]) + " baht",
               "Please choose the method calculation:",
               "1. " + cal[1], "2. " + cal[2]]
        # Choose calculation option and kind of petrol
        while not (n.isnumeric() and int(n) in [1, 2]):
            ask(sizex, sizey, set)
            n = input()
        n = int(n)

        set = [str(name[k]) + ' - price : ' + str(price[k]) + " baht",
               "You chose method calculation: " + cal[n],
               "Please enter the number of LITER or MONEY"]
        # Calculate total liters
        while not m.isnumeric():
            ask(sizex, sizey, set)
            m = input()
        m = float(m)
        if n == 2:
            res = round(m / price[k], 2)
            # message(k, m, res)
            set = [str(name[k]) + '- price : ' + str(price[k]) + " baht",
                   "The number of liters: " + str(res) + " l",
                   "You pay: " + str(m) + " baht",
                   "What do you want to do next?",
                   "1. Exit program", "2. Start new calculation"]
        # Calculate total money
        else:
            res = round(m * price[k], 2)
            set = [str(name[k]) + ' - price : ' + str(price[k]) + " baht",
                   "The number of liters: " + str(m) + " l",
                   "You pay: " + str(res) + " baht",
                   "What do you want to do next?",
                   "1. Exit program", "2. Start new calculation"]
        # aking for comeback main menu or exit program
        while not (c.isnumeric() and int(c) in [1, 2]):
            ask(sizex, sizey, set)
            c = input()
        if c == '1':
            check = False
