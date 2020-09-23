def wel():
    print("=" * 80)
    print("!", " " * 76, "!")
    print("!", " " * 76, "!")
    print("!", " " * 76, "!")
    print("!", " " * 23, "Welcome to our Oil Station.", " " * 24, "!")
    print("!", " " * 76, "!")
    print("!", " " * 76, "!")
    print("!", " " * 76, "!")
    print("=" * 80)


def getOilPrice():
    result = client.service.CurrentOilPrice(Language="en")
    root = etree.fromstring(result)
    for o in range(len(root)):
        if len(root[o]) == 3:
            name.append(root[o][1].text)
            price.append(float(root[o][2].text))


def menuoil():
    print("=" * 80)
    print("!", " " * 35, "MENU", " " * 35, "!")
    for i in range(1, len(name)):
        p = str(i) + " " + name[i] + "price : " + price[i] + " Baht."
        print("!" + " " * 22 + p + (59 - len(p)) * " " + "!")
    print("=" * 80)


def mes(k, m, l):
    mk = 36 - len(name[k])
    mm = 47 - len(str(m))
    ml = 43 - len(str(l))
    print("=" * 80)
    print("!" + " " * 16 + f"Select a petrol: {name[k]}." + " " * mk + "!")
    print("!" + " " * 22 + f"Litre: {l}" + " " * mm + "!")
    print("!" + " " * 22 + f"Pay: {m} Baht." + " " * ml + "!")
    print("=" * 80)


def last():
    while True:
    print("0 - Exit , 1 - back the menu.")
    F = "0"
    S = "1"
    E = input()
    while not (E in '01'):
        print("0 - Exit , 1 - back the menu.")
        E = input()
    if (E != S):
        break


if name in "main":
    check = True
    while check:
        # Information.
        wel()
        # Update data from website.
        name = ['none']
        price = [0]
        getOilPrice()
        # Print the manu.
        menuoil()
        print("Welcome to our Oil Station . . .")
        while do:
            g = '2'
            k = '0'
            # Choose option.
            print("Price to litre[0] OR Litre to price[1].")
            while g > '1' or not check_numeric(g):
                g = input("Please choose [0] or [1] : ")
            g = int(g)
            while (k == '0') or not check_numeric(k):
                k = input(f"Select a petrol: (1 - {name[k] - 1}) : ")
            k = int(k)
            # Calculate litre.
            if g == 0:
                m = input("Money : ")
                while not check_numeric(m):
                    m = input("Money : ")
                m = float(m)
                r = round(m / price[k], 2)
                mes(k, m, r)
            else:
                m = input("Litre : ")
                while not check_numeric(m):
                    m = input("Money : ")
                m = float(m)
                res = round(m * price[k], 2)
                mes(k, res, m)
        # Come back to the manu.
        if last():
            print("Thank you for using the service.")
