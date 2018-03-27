#!/usr/bin/env python
# Median Maintenance Algorithm
import heapq
INPUT_FILE = "Median.txt"
inFile = open(INPUT_FILE, 'r')

with inFile as f:
    inputNums = [int(integers.strip()) for integers in f.readlines()]

# medians = []
hlow = [] # support max
hhi = [] # support min
heapq.heapify(hlow)
heapq.heapify(hhi)
sum = 0
for xi in inputNums:
    if hhi and hhi[0] < xi:
        heapq.heappush(hhi, xi)
    else:
        heapq.heappush(hlow, -xi)
    # rebalance
    if (len(hhi) - len(hlow)) > 1:
        heapq.heappush(hlow, (heapq.heappop(hhi)*-1))
    elif (len(hlow) - len(hhi)) > 1:
        heapq.heappush(hhi, (heapq.heappop(hlow)*-1))
    # get the median
    if len(hhi) > len(hlow):
        # medians.append(hhi[0])
        sum += hhi[0]
    else:
        # medians.append(-(hlow[0]))
        sum += -hlow[0]
print(sum)
print(sum%10000)
