"""
#
# @File         : sample_elif.py
# @Created      : 2021-09-27 10:35
# @Author       : Bubashankushan B
# @Version      : v1.0.0
# @Licensing    : 
#
# @Description  :
#
"""

if __name__ == '__main__':
    grade = 70
    module = "python"

    if grade >= 70 and module == "python":
        print("You got an Distinction")
    elif grade >= 60 and module == "python":
        print("M.1")
    elif grade >= 50 and module == "python":
        print("M.2")
    elif grade >= 40 and module == "python":
        print("M.3")
    else:
        print("Try Again")
