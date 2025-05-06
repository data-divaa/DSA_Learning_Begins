'''
Date - 05 - May - 2025
Author - Data-Divaa
Desc - Convert a decimal number to binary using recursion.
'''

#function definition
def DTB(n):
    #base case
    if n > 1:
        #recusrion call
         DTB(n//2)
    print(n % 2, end = "")


#fetching input
n = int(input("enter the number (for decimal to binary conversion): "))


#function call
print("binary number of the provided decimal number",n)
DTB(10)
