import random

print("\t\tWelcome to a Classic Game of Rock, Paper, and Scissors!\t\t")
print("\tThe following player must choose a pick between: (rock, paper, and scissors).\t\n")
win_counter = 0
lose_counter = 0

while True:
    moves = ["rock", "paper", "scissors"]
    player_choice = 0
    system_choice = random.choice(moves)

    while player_choice not in moves:
        player_choice = input ("Enter your pick: ").lower()

    print ("The Player chose " + player_choice.upper() + ".\nThe System selected " + system_choice.upper() + ".\n")

    if player_choice == system_choice:
        print("It's a draw")
    elif player_choice == "rock":
        if system_choice == "paper":
            print("SYSTEM wins!")
            lose_counter += 1 
        else:
            print("PLAYER wins!")
            win_counter += 1
    elif player_choice == "paper":
        if system_choice == "rock":
            print("PLAYER wins!")
            win_counter += 1
        else:
            print("SYSTEM wins!")
            lose_counter += 1 
    elif player_choice == "scissors":
        if system_choice == "rock":
            print("SYSTEM wins!")
            lose_counter += 1 
        else:
            print("PLAYER wins!")
            win_counter += 1

    print("wins: " + str(win_counter))
    print("Loses: "+ str(lose_counter))
    retry = input("Play again? (y/n)")
    if retry.lower() != "y":
        break

print("You did well!")
