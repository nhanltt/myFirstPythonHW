import os
# from Package import getsizeterminal
import time


import os
import shlex
import struct
import platform
import subprocess


def get_terminal_size():
    # get terminal size in each OS
    current_os = platform.system()
    tuple_xy = None
    if current_os == 'Windows':
        tuple_xy = _get_terminal_size_windows()
        if tuple_xy is None:
            tuple_xy = _get_terminal_size_tput()
            # needed for window's python in cygwin's xterm!
    if current_os in ['Linux', 'Darwin'] or current_os.startswith('CYGWIN'):
        tuple_xy = _get_terminal_size_linux()
    if tuple_xy is None:
        tuple_xy = (80, 25)  # default value
    return tuple_xy


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
        pass


def _get_terminal_size_tput():
    # get terminal width
    try:
        cols = int(subprocess.check_call(shlex.split('tput cols')))
        rows = int(subprocess.check_call(shlex.split('tput lines')))
        return (cols, rows)
    except:
        pass


def _get_terminal_size_linux():
    def ioctl_GWINSZ(fd):
        try:
            import fcntl
            import termios
            cr = struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ, '1234'))
            return cr
        except:
            pass

    cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
    if not cr:
        try:
            fd = os.open(os.ctermid(), os.O_RDONLY)
            cr = ioctl_GWINSZ(fd)
            os.close(fd)
        except:
            pass
    if not cr:
        try:
            cr = (os.environ['LINES'], os.environ['COLUMNS'])
        except:
            return None
    return int(cr[1]), int(cr[0])


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


def inform(x, y, mes_set):
    os.system('cls')
    val = len(mes_set)
    col = x - 1
    row = (y - val) // 2 - 1
    print("*" * col)
    for i in range(row):
        print("*" + ' ' * (col - 2) + "*")
    for i in mes_set:
        print("*" + ' ' * (col // 2 - len(i) // 2) + i, end='')
        print(' ' * (col - (col // 2 - len(i) // 2) - len(i) - 2) + "*")
    for i in range(row - 2):
        print("*" + ' ' * (col - 2) + "*")
    print("*" + ' ' * (col // 2 - 3), end='')
    print("> \0337", end='')
    print(' ' * (col - (col // 2) - 1) + "*\n", end='')
    print("*" * col + '\0338', end='')


def check_remain(water, milk, cf_beans, cf_type):

    message = []
    c = False
    if (cf_type == 1) :
        if (water < 250) : 
            message.append("water")
            c = True
        if (cf_beans < 16):
            message.append("coffee beans")
            c = True
    elif (cf_type == 2):
        if (water < 350) : 
            message.append("water")
            c = True
        if (milk < 75) : 
            message.append("milk")
            c = True
        if (cf_beans < 20):
            message.append("coffee beans")
            c = True
    elif (cf_type == 3):
        if (water < 200) : 
            message.append("water")
            c = True
        if (milk < 100) : 
            message.append("milk")
            c = True
        if (cf_beans < 12):
            message.append("coffee beans")
            c = True
    if c : 
        return message
    else: 
        message.append("enough")
    return message



def buy(cf_type, water, milk, cf_beans, cup, money):
    # Calculate the ingredients remains
    cf_type = int(cf_type)
    message = []
    check = check_remain(water, milk, cf_beans, cf_type)
    if check == ["enough"]:
        message.append("I have enough resources, making you a coffee!")
        if (cf_type == 1):
            water -= 250
            cf_beans -= 16
            money += 4
        elif cf_type == 2:
            water -= 350
            milk -= 75
            cf_beans -= 20
            money += 7
        elif cf_type == 3:
            water -= 200
            milk -= 100
            cf_beans -= 12
            money += 6
        cup -= 1
    else:
        for i in check:
            message.append("Sorry! Not enough " + i)
    return water, milk, cf_beans, cup, money, message


def fill(w, m, cfb, cp, mn):
    w += w
    m += m
    cfb += cfb
    cp += cp
    return w, m, cfb, cp, mn


def asking(list, vari):
    while not vari.isnumeric():
        inform(sizex, sizey, mes_set)
        vari = input()
    mes_set[len(mes_set) - 1] += vari
    vari = int(vari)
    vari = int(vari)
    return vari, list

    
def main_menu():
    mes_set = ['Write action (buy, fill, take, remaining, exit): ']
    a = ''
    while a not in ['buy', 'fill', 'take','remaining', 'exit']:
        inform(sizex, sizey, mes_set)
        a = input(' ')
    mes_set[len(mes_set) - 1] += a
    return mes_set, a


if __name__ == '__main__':
    # Define original variables
    water = 400
    milk = 540
    cf_beans = 120
    cup = 9
    money = 550

    while True:
        sizex, sizey = get_terminal_size()
        # Print out welcome screen
        
        home(sizex, sizey)
        input()
        
        # Get action command from user
        mes_set, a = main_menu()

        # Sovle with command "buy"
        if a == 'buy':
            back = True
            while back and a == 'buy' :
                n = ''
                # Asking the kind of coffee
                k_c = ['none', "espresso", "latte", "cappuccino"]
                mes_set.append("What do you wawnt to buy? " +
                        "1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
                while n not in ['1', '2', '3', 'back']:
                    inform(sizex, sizey, mes_set)
                    n = input()
                if n in ['1', '2','3']:
                    water, milk, cf_beans, cup, money, message = \
                        buy(n, water, milk, cf_beans, cup, money)
                    mes_set.pop()
                    mes_set.append("Your selection: " + k_c[int(n)])
                    mes_set += message
                    inform(sizex, sizey, mes_set)
                    input()
                    back = False
                else : 
                    mes_set, a = main_menu()
                
        # Solving with command remain        
        if a == 'remaining':
            mes_set += ["The coffee machine has: ", str(water) + " of water",
               str(milk) + "  of milk", str(cf_beans) + " of coffee beans",
               str(cup) + " of disposable cups", str(money) + "  of money",
               (sizex - 4) * ' ']
            inform(sizex, sizey, mes_set)  
            input() 
        
        
        
        # Solve with command "fill"
        elif a == 'fill':
            w = m = cf = cp = ''
            mn = money
            # asking the number of water
            mes_set.append("Write how many ml of water do you want to add: ")
            w, mes_set = asking(mes_set, w)
            # asking the number of milk
            mes_set.append(" Write how many ml of milk do you want to add: ")
            m, mes_set = asking(mes_set, m)
            # asking the number of coffee beans
            mes_set.append(" Write how many grams of coffee beans " +
                       "do you want to add: ")
            cf, mes_set = asking(mes_set, cf)
            # asking the number of disposable cups
            mes_set.append(" Write how many disposable cups of coffee " +
                       "do you want to add: ")
            cp, mes_set = asking(mes_set, cp)
            time.sleep(2)
            # Call calculate function
            water, milk, coffee, cup, money = fill(w, m, cf, cp, mn)
           
        
        # Solve with command "take"
        elif a == 'take':
            mes_set.append("I gave you $" + str(money))
            money = 0
            inform(sizex, sizey, mes_set)
            input()
        
        elif a == 'exit':
            break
        
        # Asking for exit from program or continue new process
        mes_set = ["Do you want to exit(1) or start new process(2):"]
        check = ''
        while not (check.isnumeric() or check in ['1', '2']):
            inform(sizex, sizey, mes_set)
            check = input()
        if check == '1':
            break
