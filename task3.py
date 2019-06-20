#!/usr/bin/env python
count = int(input())
result = None

a = [i for i in range(10001)]

lst = []

i = 2
while i <= 10000:
    if a[i] != 0:
        lst.append(a[i])
        for j in range(i, 10001, i):
            a[j] = 0
    i += 1

lst = ''.join(map(str, lst))
n = list(map(int, input().split()))
result = ''.join([lst[n[i] - 1] for i in range(count)])

print(result)
