"""
#
# @File         : Question03.py
# @Created      : 2021-09-30 10:24
# @Author       : Bubashankushan B
# @Version      : v1.0.0
# @Licensing    : 
#
# @Description  : Question 03
#
"""

if __name__ == "__main__":
    upperCaseLetters = 0
    lowerCaseLetters = 0
    numbers = 0

    userString = input("Enter a string  :")  # Get user input from user

    for i in userString:  # iterate for each letter in the user Input
        if 'A' <= i <= 'Z':  # check for upper case letters and increase count
            upperCaseLetters += 1
        elif 'a' <= i <= 'z':  # check for lower case letters and increase count
            lowerCaseLetters += 1
        else:  # check for number and increase count
            numbers += 1

    print('Letter Counts in user string : {} =>  \t'.format(userString))  # Printing the character counts
    print("Uppercase Letters : {} \nLowercase letters : {}" .format(upperCaseLetters, lowerCaseLetters))
    print('Numbers \t : {}'.format(numbers))