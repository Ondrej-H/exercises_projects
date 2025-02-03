
cislo_radku = 1
pocet_radku = int(input("Zadejte číslicí počet řádků: "))
pocet_sloupcu = int(input("Zadejte číslicí počet sloupců: ")) - 1
for sloupec in range(pocet_radku):
    if cislo_radku == 1 or cislo_radku == pocet_radku:
        for radek in range(pocet_sloupcu):
            print("x", end=" ")
    else:
        print("x", end=(" " * (pocet_sloupcu*2 - 1)))
    print("x", end="\n")
    cislo_radku += 1
