'''
Date - 15 -june - 2025
Author - Data-Divaa
Desc - given an unsorted array and a index as partition sort the unsorted array in such a way that all the elements smaller than the partition element is in front of it and all the greater ones are after that but the order of the number do not matter only thing that matter is that smaller should in front and greater element should after.
'''

#this is naive solution
#function defintion
def PartitionArray(lst,p):
    n = len(lst)
    lst[p], lst[n-1] = lst[n-1] , lst[p]
    temp = []
    for i in lst:
        if i <= lst[n-1]:
            temp.append(i)

    for i in lst:
        if i > lst[n-1]:
            temp.append(i)

    for i in range(len(lst)):
        lst[i] = temp[i]

    return lst

#fetching input
lst = list(map(int,input("enter the element of list (space sepearted):").split()))

p = int(input("enter the partition index :"))


#function call
print(PartitionArray(lst,p))
