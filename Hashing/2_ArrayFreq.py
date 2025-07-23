'''
Date - 26 -june - 2025
Author - Data-Divaa
Desc - find the frequency of the elements of array.
'''

def ArrayFreq(lst):
    d1 = dict()
    for i in range(len(lst)):
        if lst[i] in d1.keys():
            d1[lst[i]] += 1
        else:
            d1[lst[i]] = 1
    for j in d1:
        print(j, "", d1[j])


lst = list(map(int,input("enter the list (space sepearted):").split()))


ArrayFreq(lst)
