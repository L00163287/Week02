"""
#
# @File         : Question02.py
# @Created      : 2021-09-30 10:07
# @Author       : Bubashankushan B
# @Version      : v1.0.0
# @Licensing    : 
#
# @Description  : Question 02
#
"""

if __name__ == "__main__":

    oddNumbers = 0
    evenNumbers = 0

    for i in range(1, 10, 1):
        if i % 2 == 0:  # check if the number has reminder
            evenNumbers = evenNumbers + 1
        else:
            oddNumbers = oddNumbers + 1

    print("Number of odd Numbers : {}".format(oddNumbers))
    print("Number of even Numbers : {}".format(evenNumbers))
