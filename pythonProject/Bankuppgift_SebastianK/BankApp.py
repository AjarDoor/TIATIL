import datetime


def open_bank():
    print('Write the name of your account: ')
    kund = str(input())
    saldo = 0
    newuser = True

    with open('Kunder.txt', 'r+') as file:
        for rad in file:
            rad = rad.split('|')
            if str(rad[0].strip()) == kund.strip():
                print('Welcome back, ' + kund + '\n')
                saldo = rad[1]
                newuser = False
                break

    if newuser:
        with open('Kunder.txt', 'a+') as file:
            file.write(kund + " | " + str(1000))
            print("Thank you for registering, we have given your account 1000kr as a gift!\n")
            saldo = 1000

    return kund, saldo


def mod_transaktions(name, changetype, changenum):
    with open('Transaktions.txt', 'a+') as file:
        if changetype == "add":
            file.write(name + " deposited " + str(changenum) + " into their account at "
                       + str(datetime.datetime.utcnow()) + "\n")
        else:
            file.write(name + " withdrew " + str(changenum) + " from their account at "
                       + str(datetime.datetime.utcnow()) + "\n")


def mod_bank(name, money):
    changetype = input(str('To add to your balance write "add", to subtract write "sub": '))
    changenum = int(input('How much would you like to add/subtract from your balance?: '))
    linecount = -1
    money = int(money)

    with open('Kunder.txt', 'r+') as file:
        data = file.readlines()

    with open('Kunder.txt', 'w+') as file:
        for rad in data:
            linecount += 1
            rad = rad.split('|')
            if str(rad[0].strip()) == name.strip():
                if changetype == "add":
                    money += changenum
                else:
                    money -= changenum
                data[linecount] = name + "|" + str(money) + "\n"
                file.writelines(data)
                break

    mod_transaktions(name, changetype, changenum)
    return name, money


info = open_bank()
info = mod_bank(info[0], info[1])
print(info[0] + " has " + str(info[1]) + "kr in their account")
