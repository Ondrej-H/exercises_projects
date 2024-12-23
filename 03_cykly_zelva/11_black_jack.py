from random import randint


def play_black_jack():
    score = 0
    while True:
        print(f"Your score is: {score}")
        if score == 21:
            print("You've reached the best score!")
            break
        elif score > 21:
            print(f"You've exceeded 21 points! You lost with {score} score.")
            break
        go_on = input("Do you want to continue? (y/n) > ")
        if go_on == "n":
            print(f"You end with {score} score.")
            break
        else:
            card = randint(2, 10)
            print(f"You have drew {card}.")
            score += card


play_black_jack()
