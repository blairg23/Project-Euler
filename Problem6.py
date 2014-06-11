# -*- coding: utf-8 -*-
#Problem 6 from projecteuler.com
#Author: Blair Gemmer
"""Description of Problem 6, Sum square difference:
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

#Sum of the squares of the first n numbers:
def sumOfSquares(n):
    sum = 0
    for i in range(0,n+1):
        sum += i**2
    return sum


#Square of the sum of the first n numbers:
def squareOfSum(n):
    sum = 0
    for i in range(0,n+1):
        sum += i
    sum = sum**2
    return sum

#Difference of the sum of the squares and square of the sum of the first n numbers:
def squaresDifference(n):
##    print "n = " + str(n)
##    print "sumOfSquares(n) = " + str(sumOfSquares(n))
##    print "squareOfSum(n) = " + str (squareOfSum(n))
    return abs(sumOfSquares(n) - squareOfSum(n))


n = 100
print squaresDifference(n)
