
heslo = "qwe"
zadani_hesla = "heslo zadá uzivatel"
while zadani_hesla != "q":
    zadani_hesla = input("Zadejte heslo (nebo 'q' pro ukončení): ")
    if zadani_hesla == heslo:
        print("Tajná informace.")
        exit()
    elif zadani_hesla == "q":
        exit()
    else:
        print("Nesprávné heslo.")
