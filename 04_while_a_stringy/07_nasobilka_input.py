
pocet_radku = int(input("Zadejte číslicí počet řádků: ")) + 1
pocet_sloupcu = int(input("Zadejte číslicí počet sloupců: ")) + 1

for sloupec in range(1, pocet_radku):
    for radek in range(1, pocet_sloupcu):
        print(f"{sloupec * radek}", end="   ")
    print("\n")
