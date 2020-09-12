import os
import time


def check_number(a):
    # check that input is numeric or not
    while not a.isnumeric():
        print("Please enter correctly!")
        a = input("> ")


def print_out(water, milk, cf_beans, cup, money):
    # print information of machine
    water = str(water) + " of water"
    milk = str(milk) + "  of milk"
    cf_beans = str(cf_beans) + "  of coffee beans"
    cup = str(cup) + " of disposable cups"
    money = str(money) + "  of money"
    print("#" * 120)
    print("#" + ' ' * 46 + "The coffee machine has:" + ' ' * 49 + '#')
    print("#" + ' ' * 46 + water + ' ' * (72 - len(water)) + "#")
    print("#" + ' ' * 46 + milk + ' ' * (72 - len(milk)) + "#")
    print("#" + ' ' * 46 + cf_beans + ' ' * (72 - len(cf_beans)) + "#")
    print("#" + ' ' * 46 + cup + ' ' * (72 - len(cup)) + "#")
    print("#" + ' ' * 46 + money + ' ' * (72 - len(money)) + "#")
    print("#" * 120)


def buy(water, milk, cf_beans, cup, money):
    # Take and check input about kind of coffee
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuchino:")
    s = input("> ")
    while s not in ['1', '2', '3']:
        print("Please enter correctly!")
        s = input("> ")
    print()
    # Calculate the ingredients remains and print out the information
    s = int(s)
    if s == 1:
        water -= 250
        cf_beans -= 16
        money += 4
    elif s == 2:
        water -= 350
        milk -= 75
        cf_beans -= 20
        money += 7
    elif s == 3:
        water -= 200
        milk -= 100
        cf_beans -= 12
        money += 6
    cup -= 1
    print_out(water, milk, cf_beans, cup, money)


def fill(water, milk, cf_beans, cup, money):
    # take input from keyboard, check input
    # update data and print out information
    print("Write how many ml of water do you want to add:")
    w = input("> ")
    check_number(w)
    water += int(w)
    print("Write how many ml of milk do you want to add:")
    m = input("> ")
    check_number(m)
    milk += int(m)
    print("Write how many grams of coffee beans do you want to add:")
    cfb = input("> ")
    check_number(cfb)
    cf_beans += int(cfb)
    print("Write how many disposable cups of coffee do you want to add:")
    cp = input("> ")
    check_number(cp)
    cup += int(cp)
    print_out(water, milk, cf_beans, cup, money)


def take(water, milk, cf_beans, cup, money):
    # withdrawn money, update data and print out information
    print("I gave you ${}".format(money))
    print()
    money = 0
    print_out(water, milk, cf_beans, cup, money)
    print()


if __name__ == '__main__':
    # Define variable and print out the information of cf-machine
    water = 400
    milk = 540
    cf_beans = 120
    cup = 9
    money = 550
    print_out(water, milk, cf_beans, cup, money)
    # Take requestment from keyboard
    print("Write action (buy, fill, take):")
    n = input("> ").strip()
    while n not in ['buy', 'fill', 'take']:
        print("Please enter correctly!")
        n = input("> ")
    # call function for each requestment
    if n == "buy":
        buy(water, milk, cf_beans, cup, money)
    elif n == "fill":
        fill(water, milk, cf_beans, cup, money)
    elif n == "take":
        take(water, milk, cf_beans, cup, money)
    # time.sleep(10)
    # os.system('cls')
