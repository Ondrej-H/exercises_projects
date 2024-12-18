import calculate
# řešení dle Arii:
# Slovník pro geometrická tělesa
geometric_solids = {
    "cube": {
        "volume": calculate.cube_calc_volume,
        "surface": calculate.cube_calc_surface
    },
    "cuboid": {
        "volume": calculate.cuboid_calc_volume,
        "surface": calculate.cuboid_calc_surface
    },
    "sphere": {
        "volume": calculate.sphere_calc_volume,
        "surface": calculate.sphere_calc_surface
    }
}

# Získání vstupu od uživatele
geometric_solid = input("Which geometric solid you want to calculate? Choose cube, cuboid or sphere: ")
metric = input("What do you want to calculate? Choose volume or surface: ")

# Kontrola vstupu
if geometric_solid in geometric_solids and metric in geometric_solids[geometric_solid]:
    # Získání funkce pro výpočet
    calculation_function = geometric_solids[geometric_solid][metric]

    # Získání rozměrů
    if geometric_solid == "cube":
        a = float(input("Longitude of side 'a'(use decimal point not decimal 'comma'): "))
        result = calculation_function(a)
    elif geometric_solid == "cuboid":
        a = float(input("Longitude of side 'a'(use decimal point not decimal 'comma'): "))
        b = float(input("Longitude of side 'b': "))
        c = float(input("Longitude of side 'c': "))
        result = calculation_function(a, b, c)
    elif geometric_solid == "sphere":
        r = float(input("Longitude of radius 'r': "))
        result = calculation_function(r)

    # Výpis výsledku
    print(f"{metric.capitalize()} of {geometric_solid} is {result}")

else:
    print("I don't understand that.")