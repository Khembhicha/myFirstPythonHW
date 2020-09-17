while True:
    print("================================================================================")
    print("!                                    MENU                                      !")
    print("!                        Gasoline 95  price 29.16 Bath.                        !")
    print("!                        Gasoline 91  price 25.30 Bath.                        !")
    print("!                        Gasohol  91  price 21.68 Bath.                        !")
    print("!                        Gasohol  95  price 21.2  Bath.                        !")
    print("!                        Gasoline E20 price 20.2  Bath.                        !")
    print("!                        Diesel       price 21.1  Bath.                        !")
    print("================================================================================")
    print("                  SELECT Price to litre[P] OR Litre to price[L].                ")
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
    while True :
        print("Entre to back the menu.")
        F = " "
        E = input()
        if not F in E :
            break