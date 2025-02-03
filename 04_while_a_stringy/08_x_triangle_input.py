pocet_radku = int(input("Zadejte číslicí počet řádků: "))
i = 0
for sloupec in range(pocet_radku):
    for radek in range(i):
        print("x", end=" ")
    print("x", end="\n")
    i += 1
