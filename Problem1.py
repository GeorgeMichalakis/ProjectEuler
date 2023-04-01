#!/bin/python3

import sys

def sumOf(n):
    sum_of_threes = 3 * (n // 3) * ((n // 3) + 1) // 2
    sum_of_fives = 5 * (n // 5) * ((n // 5) + 1) // 2
    sum_of_fifteens = 15 * (n // 15) * ((n // 15) + 1) // 2
    return sum_of_threes + sum_of_fives - sum_of_fifteens

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print (sumOf(n-1))


