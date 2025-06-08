'''
Date - 07 -june - 2025
Author - Data-Divaa
Desc - given one unsorted array with low, high and mid , sotr the unsorted array such as the low to mid it arraged and mid to high is arange the output should be one array which sorted completely.
'''


#function defintion
def MergeSubArrays(lst,low,high,mid):
    l1 = lst[low:mid+1]
    l2 = lst[mid+1 : high +1]

    i,j = 0,0
    out = []
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            out.append(l1[i])
            i += 1
        else:
            out.append(l2[j])
            j += 1

    while i < len(l1):
        out.append(l1[i])
        i += 1

    while j < len(l2):
        out.append(l2[j])
        j += 1

    return out


#fecthing input
lst = list(map(int,input("enter the unsorted array (s]pace seperated):").split()))

low,high,mid = map(int,input("enter the low , mid and high (space sepearted):").split())


#funxtion call
print("after sorting the given unsorted array :",MergeSubArrays(lst,low,mid,high))
