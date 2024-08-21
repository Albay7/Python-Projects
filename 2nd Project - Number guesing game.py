import random
#Opening of the program
top_range = input("Type a number: ")

#Converting the input into integer
if top_range.isdigit():
    top_range = int(top_range)

    if top_range <= 0:
        print("Print type a number larger than zero :) ")
        quit()
else:
    print("Please type a number next time ")
    quit()

#Range of the random number
random_number = (random.randint(0, top_range))

number_of_Guess = 0

#Algorithm for guessing
while True:
    number_of_Guess += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time ")
        continue
#Prompt the use if they're above or below of the random number
    if user_guess == random_number:
        print("you got it! ")
        break
    elif user_guess > random_number:
        print("You are above the random number: ")
    else:
        print("You are below the random number: ")

#printing the number guessing game
print("You got it in", number_of_Guess, "guesses")