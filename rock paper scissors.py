# players name
player1 = input("What is your name player 1: ")
player2 = input("What is your name player 2: ")
# game
game1 = input(f"Its your Turn {player1}:")
game2 = input(f"Its your Turn {player2}:")
# conditions
if game1 == "rock" and game2 == "paper":
    print(f"{player2} wins!!!!")
elif game1 == "rock" and game2 == "scissors":
    print(f"{player1} wins!!!!")
elif game1 == "rock" and game2 == "rock":
    print("The game was tied.Try again!!!!")
elif game1 == "paper" and game2 == "rock":
    print(f"{player1} wins!!!!")
elif game1 == "paper" and game2 == "scissors":
    print(f"{player2} wins!!!!")
elif game1 == "paper" and game2 == "paper":
    print("The game was tied.Try again!!!!")
elif game1 == "scissors" and game2 == "rock":
    print(f"{player2} wins!!!!")
elif game1 == "scissors" and game2 == "paper":
    print(f"{player1} wins!!!!")
elif game1 == "scissors" and game2 == "scissors":
    print("The game was tied.Try again!!!!")
else:
    print ("ERROR")