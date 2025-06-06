'''
Date - 24 - May - 2025
Author - Data-Divaa
Desc - give a list,set and tuple sort it using the inbulit python function sort() based on the length of the element
'''


def sorted_container(t1,l1,s1):
    t2 = sorted(t1)
    l2 = sorted(l1)
    s2 = sorted(s1)
    print("sorted tuple :",t2)
    print("sorted_list :",l2)
    print("sorted_set :",s2)


t1 = tuple(input("enter the tuple(space seperated): ").split())
l1 = list(input("enter the list(space seperated):").split())
s1 = set(input("enter the set (space seperated):").split())

sorted_container(t1,l1,s1)
