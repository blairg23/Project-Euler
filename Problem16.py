# -*- coding: utf-8 -*-
#Problem 16 from projecteuler.net
#Author: Blair Gemmer

"""Description of Problem 16, Power digit sum:
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
"""

from math import pow

bigNum = long(pow(2, 1000))

bigNum = str(bigNum)

sum = 0

for n in bigNum:
    sum += int(n)


print sum

