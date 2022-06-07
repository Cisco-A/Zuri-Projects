import random

#Initialization
print("Rock, Paper, Scissors")
plays = ["R", "P", "S"]

#Loop
end_of_game = False
while not end_of_game:
        
    player = input("Enter 'R' for Rock, 'P' for Paper and 'S' for Scissors: \n").upper()

    #Error message
    if player not in plays:
        print("Invalid input!")
    
    comp_choice = random.choice(plays)
    

    #Control Flow
    if player == "R" and comp_choice == "P":
        print("Player (Rock) : Computer (Paper)")
        print("Computer Wins!")
        end_of_game = True
    elif player == "P" and comp_choice == "R":
        print("Player (Paper) : Computer (Rock)")
        print("You Win!")
        end_of_game = True
    elif player == "S" and comp_choice == "P":
        print("Player (Scissors) : Computer (Paper)")
        print("You Win!")
        end_of_game = True
    elif player == "P" and comp_choice == "S":
        print("Player (Paper) : Computer (Scissors)")
        print("Computer Wins!")    
        end_of_game = True
    elif player == "R" and comp_choice == "S":
        print("Player (Rock) : Computer (Scissors)")
        print("You Win!")
        end_of_game = True
    elif player == "S" and comp_choice == "R":
        print("Player (Scissors) : Computer (Rock)")
        print("Computer Wins!")
        end_of_game = True
    elif player == comp_choice:
        print(f"Player ({player}) : Computer ({comp_choice}) ")
        print("It's A Draw!")
print("Thanks for playing!")