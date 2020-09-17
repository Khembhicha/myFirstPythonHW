while True:
    print("="*80)
    print("!", " "*35, "MENU", " "*35, "!")
    print("!", " "*22, "Gasoline 95  price 29.16 Bath.", " "*22, "!")
    print("!", " "*22, "Gasoline 91  price 25.30 Bath.", " "*22, "!")
    print("!", " "*22, "Gasohol  91  price 21.68 Bath.", " "*22, "!")
    print("!", " "*22, "Gasohol  95  price 21.2  Bath.", " "*22, "!")
    print("!", " "*22, "Gasoline E20 price 20.2  Bath.", " "*22, "!")
    print("!", " "*22, "Diesel       price 21.1  Bath.", " "*22, "!")
    print("="*80)
    print(" "*17, "SELECT Price to litre[P] OR Litre to price[L].", " "*16)
    m = input()
    Pricetolitre = "P"
    Litretoprice = "L"
    print("TYPE OIL :")
    o = input()
    if Pricetolitre in m:
        print("Price :")
    elif Litretoprice in m:
        print("Litre :")
    p = int(input())
    a = o.upper()
    d = 0
    if Pricetolitre in m:
        if "GASOLINE 95" in a:
            d = d + (p / 29.16)
            print("oil", '%.2f' % d, "litre.")
        elif "GASOLINE 91" in a:
            d = d + (p / 25.30)
            print("oil", '%.2f' % d, "litre.")
        elif "GASOHOL 91" in a:
            d = d + (p / 21.68)
            print("oil", '%.2f' % d, "litre.")
        elif "GASOHOL E20" in a:
            d = d + (p / 20.2)
            print("oil", '%.2f' % d, "litre.")
        elif "GASOHOL 95" in a:
            d = d + (p / 21.2)
            print("oil", '%.2f' % d, "litre.")
        elif "DIESEL" in a:
            d = d + (p / 21.1)
            print("oil", '%.2f' % d, "litre.")
        else:
            print("Select the type oil again.")
    elif Litretoprice in m:
        if "GASOLINE 95" in a:
            d = d + (p * 29.16)
            print("price", d, "Bath.")
        elif "GASOLINE 91" in a:
            d = d + (p * 25.30)
            print("price", d, "Bath.")
        elif "GASOHOL 91" in a:
            d = d + (p * 21.68)
            print("price", d, "Bath.")
        elif "GASOHOL E20" in a:
            d = d + (p * 20.2)
            print("price", d, "Bath.")
        elif "GASOHOL 95" in a:
            d = d + (p * 21.2)
            print("price", d, "Bath.")
        elif "DIESEL" in a:
            d = d + (p * 21.1)
            print("price", d, "Bath.")
        else:
            print("Select the price again.")
    else:
        print("please calculate again.")
    # while True :
    print("0 - Exit , 1 - back the menu.")
    F = "0"
    S = "1"
    E = input()
    while not(E in '01'):
        print("0 - Exit , 1 - back the menu.")
        E = input()
    if (E != S):
        break
