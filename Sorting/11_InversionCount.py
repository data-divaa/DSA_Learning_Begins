'''
Date - 08 -june - 2025
Author - Data-Divaa
Desc - given an unsorted array count the number of inversion in the array
'''


#main function defintion
def InversionCount(lst,l,r):
    res = 0
    if l < r:
        m = l + (r-l) //2
        res += InversionCount(lst,l,m)
        res += InversionCount(lst,m+1 ,r)
        res += Count(lst,l,m,r)
    return res



#helper function defintion
def Count(lst,l,m,r):
    l1 = lst[l:m+1]
    l2 = lst[m+1 : r+1]

    res,i,j,k = 0,0,0,l

    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            lst[k] = l1[i]
            i += 1
        else:
            lst[k] = l2[j]
            res += (len(l1) -1)
            j += 1
        k += 1

    while i < len(l1):
        lst[k] = l1[i]
        i += 1
        k += 1

    while j < len(l2):
        lst[k] = l2[j]
        j += 1
        k += 1

    return res



#fetching input
lst = list(map(int,input("enter the unsorted array (space sepearted):").split()))
l,r = map(int,input("enter the leftmost index and rightmost index (space sepearted)").split())


#function call
print("number of inversion in the array :",InversionCount(lst,l,r))
