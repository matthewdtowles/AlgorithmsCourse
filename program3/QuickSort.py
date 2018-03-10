#!/usr/bin/env python
INPUT_FILE = "QuickSort.txt"
inFile = open(INPUT_FILE, 'r')

with inFile as f:
    inputNums = [int(integers.strip()) for integers in f.readlines()]
