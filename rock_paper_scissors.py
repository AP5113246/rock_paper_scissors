import random 
import re 


user_wins = 0
computer_wins = 0
best_out_of_value = 0
BEST_TO_FORMAT = re.compile(r'^[3,5,8]$')

choices = ["rock","paper","scissors"]



def runGame():
    print("This is a rock, papers or scissors game. You can choose to make it a best out of 3, 5 or 8")
    getBestTo()
    print(f"The game is going to be the best till {best_out_of_value} !")
    while True:
        user_input = input("What do you pick? rock, papers or scissors or q for quit?: ").lower().strip()
        if user_input == "q":
            print("thanks for playing bye ~ !")
            break
        if user_input not in choices:
            print(f"{user_input} is an invalid input")
            continue
        else:
            print("+++++ COMPUTER CHOOSING +++++\n\n ")
            #Otherwise we start the game
            computer_choice = choices[random.randint(0,2)]
            print(f"The computer chooses {computer_choice} !")
            runRound(user_input,computer_choice)
            if checkForWinner(user_wins,computer_wins):
                break
            pass
    
    print("The game has finished!")
    print(f"You had {user_wins} wins")
    print(f"Computer had {computer_wins} wins")
    print("Bye ~!")

def checkForWinner(user_wins,computer_wins):
    if(computer_wins == best_out_of_value):
        print("++++Computer wins++++")
        return True
    elif(user_wins == best_out_of_value):
        print("++++User wins++++")
        return True
    return False



def runRound(user_input, computer_choice):
    global user_wins,computer_wins
    if user_input == computer_choice:
        print("It's a draw !\n\n")
    elif userWins(user_input,computer_choice):
        user_wins += 1
        print("You won that round \n\n!")
    else:
        print("Computer has won the round !\n\n")
        computer_wins += 1
    

def userWins(user_input,computer_choice):
    if user_input == "rock" and computer_choice == "scissors":
        return True
    elif user_input == "scissors" and computer_choice == "paper":
        return True
    elif user_input == "paper" and computer_choice == "rock":
        return True
    return False
        

#Get's the winning condition for the game
def getBestTo():
    while(True) :
        best_to = input("What do you want to make it best out of? Pick 3, 5 or 8: ")
        if(checkBestToInput(best_to)):
            global best_out_of_value
            best_out_of_value = int(best_to)
            return
        else:
            print("Invalid input")


#Returns True or False for a string to see if it is valid.
def checkBestToInput(best_to_input):
    BEST_TO_FORMAT = re.compile(r'^[3,5,8]$')
    is_match = BEST_TO_FORMAT.match(best_to_input)
    return False if (is_match is None) else True



if __name__ == '__main__':
    runGame()
