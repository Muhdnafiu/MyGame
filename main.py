
name = input("What is your name? ")
age = input("What is your age? ")
religion = input("Are you a muslim? ")
birth_year = input("to be sure, what is your birth year? ")
current_age = 2024 - int(birth_year)
course = name + " the beginner"
x = 10
x += 3
temperature = 40
if temperature > 30:
    print("It's a hot day")
    print("It's is sunny"),
print("done")
print("Assalamu alaikum " + name)
print("Then your current age is ", str(current_age))  # print("Then your current age is: ", current_age)
print("Barakallah")
print("Mashallah")
print("welcome")
print(course.lower())
"""
simple Calculator
"""
print("Write a no_ the calculate")
no_1 = input("First: ")
no_2 = input("Second: ")
Sum = float(no_1) + float(no_2)
print("Sum: ", str(Sum))

"""
simple QUIZ TEST
"""

print(" '''''' WELCOME TO QUIZ TEST '''''' ")
play = input("Do You Want To Play? ")
score = 0
if play.lower() != "yes":
    quit("Sorry For Disturbance 😢😔🤯")

print("Okay! Then Let's Go 👍👍🙌🎏🕶")

"""
simple Question
"""

question = input("What is PC? ")
if question.lower() == "personal computer":
    print("Correct!")
    score += 5
else:
    print("Incorrect")


print("You got " + str(score/5 * 100) + " % in your answer")

"""
simple Number Guesser
"""

import random

user_score = 0
computer_score = 0

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    
