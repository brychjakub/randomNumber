import random
import sys


options = []



def nextNum():
    i = 0
    while i <= len(options):
        ao = input("další číslo? stiskněte enter nebo napište n ")

        if ao == "":
                newNum = options[i]
                print(f"vyhrává číslo {newNum}")
                i += 1
                print(ao)
                if i == len(options):
                    print("* hotovo, čísla došla *")
                    sys.exit()
                else:
                    continue
        elif ao == "n":
            sys.exit()


def randomNumber():
    while True:
        try:
            num = int(input("zvolte nejvyšší číslo" + "\n"))
            break
        except ValueError:
            print("pište pouze celá čísla ")

    rnd = random.randint(1, num)
    print(f"vítězem je číslo {rnd}")
    options.append(rnd)
    for x in range(1, num + 1):
        if not x in options:
            options.append(x)
    options.remove(rnd)
    random.shuffle(options)
    while True:
        nextNum()


randomNumber()