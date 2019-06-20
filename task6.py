#!/usr/bin/env python
s = list(map(int, input().split()))

a = s[0]
b = s[1]

while a != 0 and b != 0:
    if a > b:
        a %= b
    else:
        b %= a

gcd = a + b
print(gcd)
