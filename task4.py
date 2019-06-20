#!/usr/bin/env python

game = input('Pleas inter values between space! ').split()

Points = []
score = 0

for i in game:
    if i == "+":
        roundScore = Points[-1] + Points[-2]
        score += roundScore
        Points.append(roundScore)
    elif i == "D":
        roundScore = Points[-1] * 2
        score += roundScore
        Points.append(roundScore)
    elif i == "C":
        score -= Points.pop()
    else:
        roundScore = int(i)
        score += roundScore
        Points.append(roundScore)

print(score)
