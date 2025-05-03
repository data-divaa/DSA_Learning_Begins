'''
Date - 26 - April - 2025
Author - Data-Divaa
Desc - write a recursive function to return the nth term in the fibonacci sequence.
'''

#function definition
def fibonacci(n):
    #base cases
    if n == 0 :
        return 0
    if n == 1 :
        return 1
    #recursive  call
    return fibonacci(n-1) + fibonacci(n-2)

#fetching input
n = int(input("enter the number :"))

#function call
print("the ",n,"th term in fibonacci sequence is :",fibonacci(n))
