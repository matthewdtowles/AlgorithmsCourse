#!/usr/bin/env python
INPUT_FILE = "IntegerArrayOrig.txt"
inFile = open(INPUT_FILE, 'r')

with inFile as f:
    inputNums = [int(integers.strip()) for integers in f.readlines()]

def mergeSort(inlist):
    if len(inlist) <= 1:
        return inlist
    midpoint = len(inlist) // 2
    left = inlist[:midpoint]
    right = inlist[midpoint:]

    mergeSort(left)
    mergeSort(right)

    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        print(str(k) + ' ' + str(inlist))
        if left[i] < right[j]:
            inlist[k] = left[i]
            i += 1
        else:
            inlist[k] = right[j]
            j += 1
        k += 1
    # when either i = lenleft or j = lenright:
    while i < len(left):
        inlist[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        inlist[k] = right[j]
        j += 1
        k += 1
    return inlist

# test:
print(mergeSort(inputNums))
