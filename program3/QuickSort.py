#!/usr/bin/env python
INPUT_FILE = "QuickSort.txt"
inFile = open(INPUT_FILE, 'r')

with inFile as f:
    inputNums = [int(integers.strip()) for integers in f.readlines()]

def quicksort(arr, lo, hi):
    if hi > lo:
        pivotPosition = partition(arr, lo, hi)
        quicksort(arr, lo, pivotPosition - 1)
        quicksort(arr, pivotPosition + 1, hi)


def partition(arr, lo, hi):
    pivotVal = arr[lo]
    # i is position 1 to the right of pivot
    # pivot will be moved each partition to i-1
    # j is iterator for for loop
    i = j = lo + 1
    while j <= hi:
        print(str(j)+': '+str(arr[j]))
        if arr[j] < pivotVal:
            arr[j], arr[i] = arr[i], arr[j]
            print(arr)
            i += 1
        j += 1

    # swap last item on left half with pivot
    # do this because pivot must be separator for left and right
    arr[lo], arr[i - 1] = arr[i - 1], arr[lo]
    pivotPosition = i - 1
    return pivotPosition



quicksort(inputNums, 0, len(inputNums) - 1)
print(inputNums[0])
print(inputNums[1])
print(inputNums[2])
