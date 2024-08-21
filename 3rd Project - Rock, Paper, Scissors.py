import random
#Opening of the Program

#for storing
user_wins = 0
comp_wins = 0
draws = 0
options = ["rock", "paper", "scissors"]

#Actual Algorithm
while True:
    #asking the user's input
    user_input = input("Pick your choice Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    #Generating random guess
    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    comp_guess = options[random_number]
    print("Computer Picked: ", comp_guess)

    if user_input == "rock" and comp_guess == "scissors":
        print("You Won! ")
        user_wins += 1

    elif user_input == "paper" and comp_guess == "rock":
        print("You won! ")
        user_wins +=1

    elif user_input == "scissors" and comp_guess == "paper":
        print("You won! ")
        user_wins +=1

    elif user_input == comp_guess:
        print("Draw! ")
        draws += 1

    else:
        print("You Lose! ")
        comp_wins += 1
#Printing the results
print("\n")
print("You won:", user_wins,"vs Computer won:", comp_wins, "and Draw of:", draws)
print("Thank You for Playing! ")

