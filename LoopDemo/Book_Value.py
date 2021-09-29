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

Total = 0.0  # Define total at 0

print("Book Name \t Book Price \t Running Total")
print("-"*43)
for i in range(1, 6, 1):  # Iterate loop 5 times
    bookName = str(input("Enter Book Name: "))  # get book Name
    bookValue = float(input("Enter Book price: "))  # get book Price
    Total = Total + bookValue  # Calculate running total by adding previous total and new book value
    print(bookName + "\t" + str(bookValue) + "\t" + str(Total))  # print total


