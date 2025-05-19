'''
Date - 13 - May - 2025
Author - Data-Divaa
Desc - given a number find its square root if a perfect square root is not found use the next closest floor
'''


#function defintion
def SqRoot(n):
    low = 1
    high = n
    ans = -1
    while low <= high:
        mid = (low + high ) //2
        midSq = mid * mid
        if midSq == n:
            return mid
        elif midSq > n:
            high = mid - 1
        else:
            low = mid + 1
            ans = mid
    return ans


#fetching inputs
n = int(input("enter the number whose sqaure root is to be find :"))


print("square root of n :",SqRoot(n))
