# Uppgift 1
def upg1():
    print("Uppgift 1\n")
    summa = 1
    for i in range(1, 10, 2):
        print(i)
        summa = i * summa
    print(summa)


# Uppgift 2
def upg2():
    print("\nUppgift 2\n")
    saldo = 10000
    for a in range(0, 15):
        saldo = saldo * 1.03
    print(saldo)


# Uppgift 3
def upg3():
    print("\nUppgift 3\n")
    multy = 1
    table = ""
    tablesize = int(input("Skriv ditt talbas för tabellen: "))
    print("Multiplikationstabell")
    for b in range(0, tablesize):
        multx = 1
        for c in range(0, tablesize):
            sumofxy = multx * multy
            table += " {0:>3}".format(sumofxy)
            multx += 1
        multy += 1
        table += "\n"
    print(table)


# Uppgift 4
def upg4():
    print("\nUppgift 4\n")

    upg4tal = 10
    upg4sum = 1

    while upg4tal >= 1:
        print(upg4tal)
        upg4sum *= upg4tal
        upg4tal -= 1
    print(upg4sum)


# Uppgift 5
def upg5():
    upg5rats = 100
    upg5months = 0
    while upg5rats < 1000000:
        upg5months += 1
        upg5rats *= 2
    print("After " + str(upg5months) + " months, the population of rats has exceeded 1 million")


# Uppgift 8
def upg8():
    upg8list = []
    upg8input = int(input("Skriv in heltal, skriv '0' för att avsluta: "))
    upg8max = upg8input
    upg8min = upg8input
    upg8sum = 0

    while upg8input != 0:
        upg8list.append(upg8input)
        upg8input = int(input())

    for upg8val in upg8list:
        upg8sum += upg8val
        if upg8val < upg8min:
            upg8min = upg8val
        if upg8val > upg8max:
            upg8max = upg8val

    print("Summan av talen är: " + str(upg8sum))
    print("Det minsta talet är: " + str(upg8min))
    print("Det största talet är: " + str(upg8max))


def area():
    while True:
        try:
            print("Please input the dimensions for the rectangle, with no decimals.")
            sidex = int(input("Length of X axis: "))
            sidey = int(input("Length of Y axis: "))
            break
        except:
            print("There has been an error in your inputs, please try inputting a rounded number.")
    area = sidex * sidey
    if sidex == sidey:
        result = "The area of this {} by {} square is: ".format(sidex, sidey) + str(area) + " units"
    else:
        result = "The area of this {} by {} rectangle is: ".format(sidex, sidey) + str(area) + " units"
    return area, result


def volume():
    while True:
        try:
            print("Please input the height of your rectangle, with a rounded number")
            height = int(input("Height of the rectangle: "))
            break
        except:
            print("There has been an error in your input, please try inputting a rounded number.")

    if height < 0:
        height = 1
    elif height > 10:
        height = 10
    xy = area()
    volumetable = xy[1] + "\nHeight | Volume"
    for h in range(0, height):
        volume = xy[0] * (h + 1)
        volumetable += "\n   {}   |   {} ".format(h + 1, volume)
    return volumetable


def handin2():
    restart = "Yes"
    output = ""

    while restart == "Yes":
        output += volume() + "\n"
        restart = input("Do you want to make another rectangle? Write 'Yes' to continue\n"
                        "or write anything else and return your results: ")
    print(output)


handin2()
