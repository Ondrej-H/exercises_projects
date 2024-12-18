
heslo = "qwe"
zadani_hesla = "heslo zadá uzivatel"
opakovat_zadani = ""
while opakovat_zadani == "":
    zadani_hesla = input("Zadejte heslo: ")
    if zadani_hesla == heslo:
        print("Tajná informace.")
        exit()
    else:
        print("Nesprávné heslo.")
        opakovat_zadani = input("""
Další pokus -> enter.
Ukončit -> 'q' a enter.
""")