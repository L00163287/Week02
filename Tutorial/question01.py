"""
#
# @File         : question01.py
# @Created      : 2021-09-30 09:40
# @Author       : Bubashankushan B
# @Version      : v1.0.0
# @Licensing    : 
#
# @Description  : Tutorial question 01
#
"""

if __name__ == "__main__":

    i = 1
    while i < 3:
        print("The loop starts here")
        if i == 1:
            print("This statement will always print!")
            # break  # loop doesnt iterate, and stops the condition validation
            # pass  # this completes the whole loop, almost nothing happens
            # continue  # if statement will not break and keep looping
            print("This statement will print only if it passes the above keywords")
        elif i != 1:
            print("This statement will not print if i != 1")
        print("This statement prints if the statement doesn't break")
        i = i + 1  # make sure loop ends
    print("Program ended successfully")
