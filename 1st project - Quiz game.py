#Opening Question of the program
print("Welcome to my computer quiz")
playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()
print("Okay! Let's play: ")

#Tracker of the Score
score = 0

#First Question
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct answer! ")
    score += 1
else:
    print("Wrong answer! ")
    print("The right answer is Central Processing Unit")

#Second Question
answer = input("What the GPU stands for? ")
if answer.lower() == "graphics processing unit ":
    print("Correct answer! ")
    score += 1
else:
    print("Wrong answer! ")
    print("The right answer is Graphics Processing Unit")

#Third Question
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct answer! ")
    score += 1
else:
    print("Wrong answer! ")
    print("The right answer is Random Access Memory ")

#Fourth Question
answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit ":
    print("Correct answer! ")
    score += 1
else:
    print("Wrong answer! ")
    print("The right answer is Power Supply Unit")

#Printing the Score
print("You got " + str(score) + " question correct! ")
print("You got " + str((score / 4) * 100) + "%")