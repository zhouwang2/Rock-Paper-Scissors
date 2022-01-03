import random

options = ["rock", "paper", "scissors"]

def main():
        
    computer = random.choice(options)

    player = input("Your turn: ")
    print("Computer turn: " + computer)

    if player == computer:
        print("Draw")
        main()

    elif player == "rock" and computer == "scissors":
        print("Player wins")
        main()
        
    elif player == "scissors" and computer == "paper":
        print("Player wins")
        main()
                  
    elif player == "paper" and computer == "rock":
        print("Player wins")
        main()
            
    elif player == "paper" and computer == "scissors":
        print("Computer wins")
        main()
            
    elif player == "scissors" and computer == "rock":
        print("Computer wins")
        main()
            
    elif player == "rock" and computer == "paper":
        print("Computer wins")
        main()
main()
