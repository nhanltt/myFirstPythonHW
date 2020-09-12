def print_out(water, milk, cf_beans, cup, money):
    print("The coffee machine has:")
    print("{} of water".format(water))
    print("{} of milk".format(milk))
    print("{} of coffee beans".format(cf_beans))
    print("{} of disposable cups".format(cup))
    print("{} of money".format(money))
    print()


def buy(water, milk, cf_beans, cup, money):
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuchino:")
    s = int(input("> "))
    print()
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
    print()


def fill(water, milk, cf_beans, cup, money):
    print("Write how many ml of water do you want to add:")
    water += int(input("> "))
    print("Write how many ml of milk do you want to add:")
    milk += int(input("> "))
    print("Write how many grams of coffee beans do you want to add:")
    cf_beans += int(input("> "))
    print("Write how many disposable cups of coffee do you want to add:")
    cup += int(input("> "))
    print()
    print_out(water, milk, cf_beans, cup, money)
    print()


def take(water, milk, cf_beans, cup, money):
    print("I gave you ${}".format(money))
    print()
    money = 0
    print_out(water, milk, cf_beans, cup, money)
    print()


if __name__ == '__main__':
    water = 400
    milk = 540
    cf_beans = 120
    cup = 9
    money = 550
    print_out(water, milk, cf_beans, cup, money)
    print("Write action (buy, fill, take):")
    n = input("> ")
    if n == "buy":
        buy(water, milk, cf_beans, cup, money)
    elif n == "fill":
        fill(water, milk, cf_beans, cup, money)
    elif n == "take":
        take(water, milk, cf_beans, cup, money)
