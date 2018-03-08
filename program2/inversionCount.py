#!/usr/bin/env python
INPUT_FILE = "IntegerArrayOrig.txt"
inFile = open(INPUT_FILE, 'r')

with inFile as f:
    inputNums = [int(integers.strip()) for integers in f.readlines()]

count = 0

def invCount(arrayIn):
    if len(arrayIn) <= 1:
        return 0;
    global count

    middle = len(arrayIn) // 2
    left = arrayIn[:middle]
    right = arrayIn[middle:]

    invCount(left)
    invCount(right)

    # Merge sorted sub-arrays and keep count
    i, j = 0, 0
    for k in range(len(left) + len(right) + 1):
        if left[i] <= right[j]:
            arrayIn[k] = left[i]
            i += 1
            if i == len(left) and j != len(right):
                while j != len(right):
                    k +=1
                    arrayIn[k] = right[j]
                    j += 1
                break
        else:
            arrayIn[k] = right[j]
            count += (len(left) - i)
            j += 1
            if j == len(right) and i != len(left):
                while i != len(left):
                    k+= 1
                    arrayIn[k] = left[i]
                    i += 1
                break
    return count


print (invCount(inputNums))
