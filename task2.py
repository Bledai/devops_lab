#!/usr/bin/env python
import math
sumMain = 0
sumSecond = 0
lens = int(input())
matrix = []
for i in range(lens):
    matrix.append(list(map(int, input().split())))

for i in range(lens):
    sumMain += matrix[i][i]
    sumSecond += matrix[i][lens - i - 1]
print('%.0f' % math.fabs(sumMain - sumSecond))
