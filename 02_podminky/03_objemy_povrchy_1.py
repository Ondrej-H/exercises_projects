import calculate
# This is primarily exercise for if statements:

# geometric solid znamená geometrické těleso
geometric_solid = ""
while geometric_solid != "cube" and geometric_solid != "cuboid" and geometric_solid != "sphere":
    geometric_solid = input("Which geometric solid you want to calculate? Choose cube, cuboid or sphere: ") # cuboid znamená obdélník

metric = ""
while metric != "volume" and metric != "surface":
    metric = input("What do you want to calculate? Choose volume or surface: ")

if geometric_solid == "cube":
    a = float(input("Longitude of side 'a'(use decimal point not decimal 'comma'): "))
    if metric == "volume":
        print(f"Volume of {geometric_solid} with a = {a} is {(calculate.cube_calc_volume(a))}")
    elif metric == "surface":
        print(f"Surface of {geometric_solid} with a = {a} is {(calculate.cube_calc_surface(a))}")
    else:
        print("I don't understand that.")

elif geometric_solid == "cuboid":
    a = float(input("Longitude of side 'a'(use decimal point not decimal 'comma'): "))
    b = float(input("Longitude of side 'b': "))
    c = float(input("Longitude of side 'c': "))
    if metric == "volume":
        print(f"Volume of {geometric_solid} with a = {a}, b = {b}, c = {c} is {(calculate.cuboid_calc_volume(a,b,c))}")
    elif metric == "surface":
        print(f"Surface of {geometric_solid} with a = {a}, b = {b}, c = {c} is {(calculate.cuboid_calc_surface(a,b,c))}")
    else:
        print("I don't understand that.")

elif geometric_solid == "sphere":
    r = float(input("Longitude of radius 'r': "))       # radius znamená poloměr
    if metric == "volume":
        print(f"Volume of {geometric_solid} with r = {r} is {(calculate.sphere_calc_volume(r))}")
    elif metric == "surface":
        print(f"Surface of {geometric_solid} with r = {r} is {(calculate.sphere_calc_surface(r))}")

else:
    print("I don't understand that.")
