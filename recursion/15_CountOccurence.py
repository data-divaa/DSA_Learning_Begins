'''
Date - 06 - May - 2025
Author - Data-Divaa
Desc - Write a recursive function to count how many times a value appears in a list.
Example: count_occurrences([1, 2, 1, 3], 1) → 2
'''

#function defintion
def CountOccurrence(lst,n):
    #base case
    if len(lst) == 0:
        return 0
    if lst[0] == n:
        #add and call recursively
        return 1 + CountOccurrence(lst[1:],n)
    else:
        #call without ading
        return CountOccurrence(lst[1:],n)

#fetchinf details
lst = list(map(int,input("enter the number list (space seperated):").split()))
n = int(input("enter the number :"))

#function call
print("number of times",n, "occureed in ",lst, ":" ,CountOccurrence(lst,n))
