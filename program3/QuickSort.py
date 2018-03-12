#!/usr/bin/env python
INPUT_FILE = "QuickSort.txt"
inFile = open(INPUT_FILE, 'r')

with inFile as f:
    inputNums = [int(integers.strip()) for integers in f.readlines()]


def quicksort(arr, lo, hi):
    if hi > lo:
        # change which parition below
        pivotPosition = partition(arr, lo, hi, partitionmid)
        quicksort(arr, lo, pivotPosition - 1)
        quicksort(arr, pivotPosition + 1, hi)


def partitionlo(arr, lo, hi):
    pivotVal = arr[lo]
    # i is position 1 to the right of pivot
    # pivot will be moved each partition to i-1
    # j is iterator for for loop
    i = j = lo + 1
    while j <= hi:
        if arr[j] < pivotVal:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
        j += 1
    # swap last item on left half with pivot
    # do this because pivot must be separator for left and right
    arr[lo], arr[i - 1] = arr[i - 1], arr[lo]
    pivotPosition = i - 1
    return pivotPosition


def partitionhi(arr, lo, hi):
    pivotVal = arr[hi]
    i = j = lo
    while j < hi:
        if arr[j] < pivotVal:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
        j += 1
    # swap first item on right half with pivot
    arr[hi], arr[i] = arr[i], arr[hi]
    pivotPosition = i
    return pivotPosition


def partitionmid(arr, lo, hi):
    mid = int((hi - lo)//2)
    pivotVal = sorted((arr[lo], arr[mid], arr[hi]))[1]
    if pivotVal == arr[lo]:
        return partitionlo(arr, lo, hi)
    elif pivotVal == arr[hi]:
        return partitionhi(arr, lo, hi)
    arr[lo], arr[mid] = arr[mid], arr[lo]
    return partitionlo(arr, lo, hi)


def partition(arr, lo, hi, option):
    return option(arr, lo, hi)


quicksort(inputNums, 0, len(inputNums) - 1)
# print(inputNums)
