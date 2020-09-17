while True:
    ow = int(400)
    om = int(540)
    oc = int(120)
    od = int(9)
    omn = int(550)
    print("="*80)
    print("|", " "*27, "The coffee machine has :", " "*23, "|")
    print("|", " "*24, ow, "of water.", " "*37, "|")
    print("|", " "*24, om, "of milk.", " "*38, "|")
    print("|", " "*24, oc, "of coffee beans.", " "*30, "|")
    print("|", " "*24, od, "of disposable cups.", " "*29, "|")
    print("|", " "*24, omn, "of money.", " "*37, "|")
    print("="*80)
    print("")
    b = "buy"
    f = "fill"
    t = "take"
    espresso = "1"
    latte = "2"
    cappuccino = "3"
    print("Write action ( buy , fill , take ) :")
    wa = str(input("> "))
    if b in wa:
        print("What do you want to buy? 1 - espresso , 2 - latte , 3 - cappuccino")
        wb = str(input())
        print("")
        if espresso in wb:
            print("The coffee machine has :")
            print(ow - 250, "of water.")
            print(om, "of milk.")
            print(oc - 16, "of coffee beans.")
            print(od - 1, "of disposable cups.")
            print(omn + 4, "of money.")
        elif latte in wb:
            print("The coffee machine has :")
            print(ow - 350, "of water.")
            print(om - 75, "of milk.")
            print(oc - 20, "of coffee beans.")
            print(od - 1, "of disposable cups.")
            print(omn + 7, "of money.")
        elif cappuccino in wb:
            print("The coffee machine has :")
            print(ow - 200, "of water.")
            print(om - 100, "of milk.")
            print(oc - 12, "of coffee beans.")
            print(od - 1, "of disposable cups.")
            print(omn + 6, "of money.")
    elif f in wa:
        print("Write how many ml of water do you want to add :")
        adw = int(input("> "))
        print("Write how many ml of milk do you want to add :")
        adm = int(input("> "))
        print("Write how many grams of coffee beans do you want to add :")
        adcb = int(input("> "))
        print("Write how many disposable cups of coffee do you want to add :")
        adc = int(input("> "))
        print("")
        print("The coffee machine has :")
        print(ow + adw, "of water.")
        print(om + adm, "of milk.")
        print(oc + adcb, "of coffee beans.")
        print(od + adc, "of disposable cups.")
        print(omn, "of money.")
    elif t in wa:
        print("I gave you $", omn)
        print("")
        print("The coffee machine has :")
        print(ow, "of water.")
        print(om, "of milk.")
        print(oc, "of coffee beans.")
        print(od, "of disposable cups.")
        print(omn - omn, "of money.")
    print("0 - Exit , 1 - back the menu.")
    F = "0"
    S = "1"
    E = input()
    while not (E in '01'):
        print("0 - Exit , 1 - back the menu.")
        E = input()
    if E != S:
        break
