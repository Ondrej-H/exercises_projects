from random import randrange
# rock, paper, scicors
def play(players_turn):
    rand_num = randrange(3)
    if rand_num == 0:
        pcs_turn = "rock"
    elif rand_num == 1:
        pcs_turn = "paper"
    else:
        pcs_turn = "scisors"
    print(pcs_turn)

    if players_turn == pcs_turn:
        print("It's tie!")
    elif (players_turn, pcs_turn) == ("rock", "scisors") or \
        (players_turn, pcs_turn) == ("scisors", "paper") or \
        (players_turn, pcs_turn) == ("paper", "rock"):
        print("You won!")
    elif (pcs_turn, players_turn) == ("rock", "scisors") or \
        (pcs_turn, players_turn) == ("scisors", "paper") or \
        (pcs_turn, players_turn) == ("paper", "rock"):
        print("PC won!")
    elif players_turn == "q":
        exit()
    else:
        print("Sorry, but I understand only three words: rock, paper, scisors!")

while True:
    players_turn = input("For exit type 'q'\nrock, paper or scisors(type)? > ")
    play(players_turn)
    if players_turn == "q":
        exit()
