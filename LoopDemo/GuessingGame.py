"""
#
# @File         : GuessingGame.py
# @Created      : 2021-09-29 22:00
# @Author       : Bubashankushan B
# @Version      : v1.0.0
# @Licensing    : 
#
# @Description  : Guessing game
#
"""

number = 8  # Number to guess
guess = False
while not guess:  # Check if the user guessed number false
    userval = int(input("Enter Value: ")) # get user value
    print("Checking ", userval)
    if userval == number:
        guess = True  # mark user guessed value True
    else:
        print("Try again...")
print("You successfully guessed the number..!!")
