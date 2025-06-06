'''
Date - 24 - May - 2025
Author - Data-Divaa
Desc - give a array sort it using the inbulit python function sort() based on the length of the element
'''

def len_ele(lst):
    return len(lst)


def sort_len(lst):
    lst.sort(key = len_ele)
    return lst

lst = list(input("enter the list (space seperated):").split())


print(sort_len(lst))
