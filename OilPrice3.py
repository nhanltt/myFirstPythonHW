import os
import time

from zeep import Client
from lxml import etree

client = Client('https://www.pttor.com/OilPrice.asmx?WSDL')
passwork = '9999'


def check_numeric(num):
    if num.isnumeric():
        return True
    else:
        print("Please enter correctly")
        return False


def home():
    print("*" * 120)
    print("*" + ' ' * 118 + '*')
    print('*' + ' ' * 50 + 'PETROL SALE SYSTEM' + ' ' * 50 + '*')
    print('*' + ' ' * 47 + 'Author: Nhan Le Thi Thanh' + ' ' * 46 + '*')
    print('*' + ' ' * 48 + 'Published at 09/01/2020' + ' ' * 47 + '*')
    print("*" + ' ' * 118 + '*')
    print("*" * 120)


def update_price():
    result = client.service.CurrentOilPrice(Language="en")
    root = etree.fromstring(result)
    for i in range(len(root)):
        if len(root[i]) == 3:
            name.append(root[i][1].text)
            price.append(float(root[i][2].text))


def menu():
    print("*" * 120)
    print("*" + ' ' * 118 + '*')
    print('*' + ' ' * 57 + 'MENU' + ' ' * 57 + '*')
    for i in range(1, len(name)):
        s = str(i) + '. ' + name[i] + ' : ' + str(price[i]) + ' BAHT'
        print('*' + 46 * ' ' + s + (72 - len(s)) * ' ' + '*')
    print("*" + ' ' * 118 + '*')
    print("*" * 120)


def check_pass(pas):
    while True:
        if check_numeric(pas):
            if pas == '1':
                return True
            elif pas == '0':
                return False
        pas = input("Are you ready to start? (Enter 1 if Yes or 0 if No): ")


def message(key, mon, lit):
    sp_k = 56 - len(name[key])
    sp_l = 48 - len(str(lit))
    sp_m = 58 - len(str(mon))
    print("*" * 120)
    print('*' + ' ' * 46 + f"Kind of petrol: {name[key]}" + " " * sp_k + '*')
    print('*' + ' ' * 46 + f"The number of liters: {lit} l" + ' ' * sp_l + '*')
    print('*' + ' ' * 46 + f"You pay: {mon} BAHT" + ' ' * sp_m + '*')
    print("*" * 120)


def respond():
    while True:
        s = int(input("Do you want to finish? Enter 1 if Yes "))
        if s == 1:
            return True


if __name__ == '__main__':

    check = True
    while check:
        # Information about program
        home()
        # Update data from website
        name = ['none']
        price = [0]
        update_price()
        # print out menu
        menu()
        # Fix home, update and menu : 16:45 - 17:30
        print("Welcome to our petrol system.")
        pas = input("Are you ready to start? (Enter 1 if Yes or 0 if No): ")
        # check passwork
        if pas == passwork:
            check = False
            break
        else:
            letgo = check_pass(pas)
        while letgo:
            n = '2'
            k = '0'
            # Choose calculation option and kind of petrol
            print("MONEY -> LITERS (0) or LITERS -> MONEY (1) ")
            while n > '1' or not check_numeric(n):
                n = input("Please choose 0 or 1: ")
            n = int(n)
            while (k == '0') or not check_numeric(k):
                k = input(f"Kind of petrol (1-{len(name) - 1}): ")
            k = int(k)
            # Calculate total liters
            if n == 0:
                m = input("Please enter the number money: ")
                while not check_numeric(m):
                    m = input("Please enter the number money: ")
                m = float(m)
                res = round(m / price[k], 2)
                message(k, m, res)
                letgo = False
            # Calculate total money
            else:
                m = input("Please enter the number liters: ")
                while not check_numeric(m):
                    m = input("Please enter the number money: ")
                m = float(m)
                res = round(m * price[k], 2)
                message(k, res, m)
                letgo = False
        # Comeback main menu
        if respond():
            print("Thank you. See you again!")
            time.sleep(3)
            os.system('cls')
