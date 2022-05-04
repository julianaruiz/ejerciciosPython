# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 21:52:15 2020

@author: JULI
"""

x = int(input('Enter a number: '))
epsilon = 0.01 #epsilon = 0.0001 #epsilon = 0.1
step = 0.0001 #step = 0.1 #step = 0.8
contador = 0
ans = 0.0
while abs(ans**2 - x) >= epsilon and ans <= x:
    ans += step
    guesses += 1

if abs(ans**2 - x) >= epsilon:
    print('Couldn\'t find the square root of', x)
else:
    print(ans, 'is approximately the square root of', x)

print('There were', guesses, 'guesses')