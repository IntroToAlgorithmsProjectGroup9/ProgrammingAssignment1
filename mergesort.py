#Source: The book, and GeeksforGeeks page on mergesort

from math import floor

# Merges two sublists of the mian list
# First sublist is list[l..m]
# Second sublist is list[m+1..r]
def merge(list,l,m,r):
    #compute sizes of the arrays given the indexes
    arr1size = m - l + 1
    arr2size = r - m

    #create temp lists of the correct sizes computed above.
    lefthandside = [0] * (arr1size)
    righthandside = [0] * (arr2size)

    #copy the elements to the temp arrays
    for x in range(0, arr1size):
        lefthandside[x] = list[l + x]

    for y in range(0, arr2size):
        righthandside[y] = list[m+1+y]

    leftsideindex = 0
    rightsideindex= 0
    sortedlistindex = l

    #actually merge the two sublists into one main list.
    while leftsideindex < arr1size and rightsideindex <arr2size:
        if lefthandside[leftsideindex] <= righthandside[rightsideindex]:
            list[sortedlistindex] = lefthandside[leftsideindex]
            leftsideindex += 1
        else:
            list[sortedlistindex] = righthandside[rightsideindex]
            rightsideindex += 1
        sortedlistindex += 1

    #Copy any remaining elements of either subarrays
    while leftsideindex < arr1size:
        list[sortedlistindex] = lefthandside[leftsideindex]
        leftsideindex += 1
        sortedlistindex += 1
    while rightsideindex < arr2size:
        list[sortedlistindex] = righthandside[rightsideindex]
        rightsideindex += 1
        sortedlistindex += 1


def mergesort(list,leftindex,rightindex):
    #test to make sure theirs sorting to be done.
    #if so, compute middle, and then recurse.
    #then, merge both the sides.
    if leftindex < rightindex:
        midpoint = floor((leftindex+rightindex)/2)
        mergesort(list,leftindex,midpoint)
        mergesort(list, midpoint + 1, rightindex)
        merge(list,leftindex, midpoint,rightindex)


