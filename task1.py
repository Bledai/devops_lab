#!/usr/bin/env python
import operator
count = int(input())
listSt = {}
marks = []
names = []
result = None
for i in range(count):
    name = input('Enter student name: ')
    mark = float(input('Enter %ss mark: ' % name))
    listSt[name] = mark

listSt = sorted(listSt.items(), key=operator.itemgetter(1))

for i in range(count):
    if listSt[i][1] != listSt[i + 1][1]:
        result = listSt[i + 1][1]
        break
for i in range(count):
    if result == listSt[i][1]:
        print(listSt[i][0])
