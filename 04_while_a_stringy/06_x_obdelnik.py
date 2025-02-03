
cislo_radku = 1
i = 5
for delka_sloupce in range(6):
    if cislo_radku == 1 or cislo_radku == 6:
        for radek in range(5):
            print("x", end=" ")
    else:
        print("x", end="         ")
    print("x", end="\n")
    cislo_radku += 1
