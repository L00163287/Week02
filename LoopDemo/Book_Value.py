"""
#
# @File         : Book_Value.py
# @Created      : 2021-09-29 22:08
# @Author       : Bubashankushan B
# @Version      : v1.0.0
# @Licensing    : 
#
# @Description  : Calculate total values of books (Question 02)
#
"""

book1 = "Sherlock Holmes 1"
book2 = "Sherlock holmes 2"
book3 = "Learn Java"
book4 = "Learn python"
book5 = "Tale of two cities"

book1val = 10.50
book2val = 11.50
book3val = 22.50
book4val = 20.50
book5val = 10

Total = 0.0

for i in range(1, 6, 1):
    print(str(book1) + "\t" + str(book1val) + "\t" + str(Total + book1val))
