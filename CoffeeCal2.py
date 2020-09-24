import os
from Package import getsizeterminal


def home(sizex, sizey):
    os.system('cls')
    row = sizey // 2 - 3
    col = sizex - 1
    print("*" * (col))
    for i in range(row):
        print("*" + ' ' * (col - 2) + '*')
    print('*' + ' ' * (col // 2 - 13) + "AUTOMATIC COFFEE MACHINE", end='')
    print(' ' * (col - col // 2 - 13) + '*')
    print('*' + ' ' * (col // 2 - 13) + 'Author: Nhan Le Thi Thanh', end='')
    print(' ' * (col - col // 2 - 14) + '*')
    print('*' + ' ' * (col // 2 - 12) + 'Published at 09/23/2020', end='')
    print(' ' * (col - col // 2 - 13) + '*')
    print("*" + ' ' * (col - 2) + '*')
    print("*" + ' ' * (col - 2) + '*')
    print("*" + ' ' * (col - 2) + '*')
    print("*" + ' ' * (col // 2 - 25) + "WELCOME TO OUR SYSTEM!", end='')
    print(' PLEASE PRESS ANY KEY TO CONTINUE...\0337', end='')
    print(' ' * (col - col // 2 - 35) + "*")
    for i in range(row - 3):
        print("*" + ' ' * (col - 2) + '*')
    print("*" * (col) + '\0338', end='')


def inform(x, y, set):
    os.system('cls')
    val = len(set)
    col = x - 1
    row = (y - val) // 2 - 1
    print("*" * col)
    for i in range(row):
        print("*" + ' ' * (col - 2) + "*")
    for i in set:
        print("*" + ' ' * (col // 2 - len(i) // 2) + i, end='')
        print(' ' * (col - (col // 2 - len(i) // 2) - len(i) - 2) + "*")
    for i in range(row - 2):
        print("*" + ' ' * (col - 2) + "*")
    print("*" + ' ' * (col // 2 - 3), end='')
    print("> \0337", end='')
    print(' ' * (col - (col // 2) - 1) + "*\n", end='')
    print("*" * col + '\0338', end='')


def buy(s, water, milk, cf_beans, cup, money):

    # Calculate the ingredients remains
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
    return water, milk, cf_beans, cup, money


def fill(w, m, cfb, cp, mn):
    w += w
    m += m
    cfb += cfb
    cp += cp
    return w, m, cfb, cp, mn


def asking(x,y,list,vari):
    while not vari.isnumeric():
        inform(sizex, sizey, set)
        vari = input()
    set[len(set) - 1] += vari
    vari = int(vari)
    vari = int(vari)
    return vari, list


if __name__ == '__main__':
    # Define original variables
    water = 400
    milk = 540
    cf_beans = 120
    cup = 9
    money = 550
    while True:
        sizex, sizey = getsizeterminal.get_terminal_size()
        # Print out welcome screen
        home(sizex, sizey)
        input()
        set =[ "The coffee machine has: ", str(water) + " of water", str(milk) + "  of milk",
               str(cf_beans) + " of coffee beans", str(cup) + " of disposable cups",
               str(money) + "  of money", (sizex - 4)*' ', "Write action (buy, fill, take): "]
        # Get action command from user
        a = ''
        while a not in ['buy', 'fill', 'take']:
            inform(sizex, sizey, set)
            a = input()
        set[len(set) - 1] += a
        # Sovle with command "buy"
        if a == 'buy':
            n = ''
            # Asking the kind of coffee
            set.append("What do you wawnt to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
            while n not in ['1','2','3']:
                inform(sizex, sizey, set)
                n = input()
            water, milk, cf_beans, cup, money = buy(n, water, milk, cf_beans, cup, money)
        # Solve with command "fill"
        elif a == 'fill':
            w = m = cf = cp = ''
            mn = money
            # asking the number of water
            set.append("Write how many ml of water do you want to add: ")
            w, set = asking(sizex, sizey, set, w)
            # asking the number of milk
            set.append(" Write how many ml of milk do you want to add: ")
            m, set = asking(sizex, sizey, set, m)
            # asking the number of coffee beans
            set.append(" Write how many grams of coffee beans do you want to add: ")
            cf, set = asking(sizex, sizey, set, cf)
            # asking the number of disposable cups
            set.append(" Write how many disposable cups of coffee do you want to add: ")
            cp, set = asking(sizex, sizey, set, cp)
            # Call calculate function
            water, milk, coffee, cup, money = fill(w, m, cf, cp, mn)
        # Solve with command "take"
        elif a == 'take':
            set.append("I gave you $" + str(money))
            money = 0
            inform(sizex, sizey, set)
        input()
        # Asking for exit from program or continue new process
        set = ["The coffee machine has: ", str(water) + " of water", str(milk) + "  of milk",
               str(cf_beans) + " of coffee beans", str(cup) + " of disposable cups",
               str(money) + "  of money", (sizex - 4) * ' ', "Do you want to exit(1) or start new process(2):"]
        check = ''
        while not(check.isnumeric() or check in ['1', '2']):
            inform(sizex, sizey, set)
            check = input()
        if check == '1':
            break







