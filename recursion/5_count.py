'''
Date - 27 - April - 2025
Author - Data-Divaa
Desc -
Write a recursive function that returns the number of digits in a number.
'''

def count(n):
    if n == 0:
        return 0
    return 1 + count(n // 10)


n = int(input("enter the number:"))

print("the number of digits in the number ",n," : ",count(n))
