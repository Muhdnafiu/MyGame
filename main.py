# name = input("What is your name? ")
# color = input("What is your favorite color? ")
# print(name  + ' likes ' + color)
# weight_in_pounds = input('What is your weight(Lbs)? ')
# weight_in_Kilogram = int(weight_in_pounds) *  0.45
# print(f"You Are {weight_in_Kilogram} kg")
# weight = input("Weight: ")
# unit = input("(L)bs Or (K)g: ")
# if unit.upper== "L":
#     converted = weight * 0.45
#     print(f"You are {converted} Kilos")
# else:
#     converted = weight / 0.45
#     print(f"You Are {converted.float}  Pounds")

# import random
# number_to_guess = random.randint(0,100)
# while True:
#     try:
#         number = int(input("Guess the number btw 1 and 100: "))
#     except ValueError:
#         print("Please Enter a Valid Number.")

#     if number == number_to_guess :
#         print("Congratulations! you guessed the number")
#         break
#     elif number <= number_to_guess:
#         print("Too Low.")
#     elif number >= 8:
#         print("Too High.")


# numbers  = ['5', '2', '5', '2', '2']
# for i in numbers:
#     print('x' * i)
def evens_and_odds(n):
    evens = len([num for num in range(n+1) if num % 2 == 0])
    odds = len([num for num in range(n+1) if num % 2 != 0])
    return evens, odds

