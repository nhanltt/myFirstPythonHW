import os
import time

from zeep import Client
from lxml import etree

client = Client('https://www.pttor.com/OilPrice.asmx?WSDL')


def respond():
    while True:
        s = int(input("Do you want to finish? Enter 1 if Yes"))
        if s == 1:
            return True


check = True
while check:
    # Comment
    print("PETROL SALE SYSTEM")
    print("Author: Nhan Le Thi Thanh ")
    print("Published at 01/09/2020")
    # Update data from website
    result = client.service.CurrentOilPrice(Language="en")
    root = etree.fromstring(result)
    n = len(root)
    name = ['none']
    price = [0]
    for i in range(n):
        if len(root[i]) == 3:
            name.append(root[i][1].text)
            price.append(float(root[i][2].text))
    print("*** MENU ***")
    for i in range(1, len(name)):
        print("{}. {} : {} BAHT".format(i, name[i], price[i]))
    print("Welcome to our petrol system.")
    pas = input("Are you ready to start? (Enter 1 if Yes or 0 if No): ")
    if pas == "9999":
        check = False
        break
    start = int(pas)
    if start == 1:
        letgo = True
    else:
        letgo = False

    while letgo:
        n = 2
        k = 0
        print("Calculate LITERS BY MONEY (0) or MONEY BY LITERS(1)? ", end=' ')
        while n > 1:
            n = int(input("Please choose 0 or 1: "))
        while k == 0:
            k = int(input(f"Please choose kind of petrol (1-{len(name)-1}): "))
        if n == 0:
            m = float(input("Please enter the number money: "))
            res = m / price[k]
            print(f"The number of liters: {res} l")
            letgo = False
        else:
            m = float(input("Please enter the number liters: "))
            res = m * price[k]
            print(f"Total price: {res} BAHT")
            letgo = False

    if respond():
        print("Thank you. See you again!")
        time.sleep(3)
        os.system('cls')
