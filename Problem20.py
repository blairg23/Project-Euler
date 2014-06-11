# -*- coding: utf-8 -*-
#Problem 20 from projecteuler.net
#Author: Blair Gemmer

"""Description of Problem 20, Factorial digit sum:
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

from math import factorial

bigNumber = factorial(100)

bigNumber = str(bigNumber)

sum = 0

for n in bigNumber:
    sum += int(n)

print sum
