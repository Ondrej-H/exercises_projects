from random import randint

print("Welcome to the Multiplication Game!")
print("Anytime you want to quit just type 'q' and press enter! ")
print("Enjoy the game!")
print()
answer = ""
while answer != "q":
    num_1 = randint(1, 10)
    num_2 = randint(1, 10)
    product = num_1 * num_2     # product je anglicky součin
    try:
        answer = int(input(f"{num_1} x {num_2} is: "))
        if answer == product:
            print("That's right! Good job!")
        else:
            print(f"Really? And in which space is that so? I thought it is {product}.")
    except ValueError:
        answer = input("Do you want to quit the game ('q' + enter)?")
        if answer == "q":
            break
        else:
            print("Your answer must be an integer or 'q' to quit the game.")
