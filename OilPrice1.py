# Create data in list
name = ['none', 'Gasoline 95', 'Gasoline 91',
        'Gasohol 91', 'Gasohol E20', 'Gasohol 95', 'Diesel']
price = [0, 29.16, 25.3, 21.68, 20.2, 21.2, 21.1]

if __name__ == '__main__':
    while True:
        print("Welcome to our petrol system!")
        # get password to start
        pas = input("Are you ready to start? 0 if no, 1 if yes: ")
        if pas == '9999':
            break
        # print out menu of petrol price
        print("      ***  MENU  ***")
        for i in range(1, len(name)):
            print(i, f'. {name[i]} : {price[i]} BAHT')
        # choose the kind of calculation method
        k = int(input("liters -> money(0) or money -> liters(1) "))
        # choose the kind of petrol
        n = int(input("What kind of petrol: "))
        # get data, calculate
        # and print out the number of liter that customer gets
        # or the number of money that customer pays
        if k == 0:
            l = float(input("Please enter the number of liters: "))
            res = l * price[n]
            print(f"You pay: {res} BAHT")
        else:
            m = float(input("Please enter the number of money: "))
            res = m / price[n]
            print(f"You get: {res} l")
        print("Thank you and see you again!")
        print("_" * 50)
        # comeback getting started
