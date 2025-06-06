'''
Date - 24 - May - 2025
Author - Data-Divaa
Desc - give an unsorted array arrange this is ascending order
'''


def BubbleSort(lst):

    for i in range(len(lst) -1):
        swap = False
        for j in range(len(lst) - i -1):
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]

                swap = True

        if not swap:
            break
    return lst


lst = [8,3,1,9]

print(BubbleSort(lst))
