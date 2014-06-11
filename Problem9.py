#Problem 9 from projecteuler.net
#Author: Blair Gemmer

"""Description of Problem 9, Special Pythagorean triplet:

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import time

def isPythagoreanTriplet(a,b,c):
    """Returns True if the triplet is of the type a^2 + b^2 = c^2 AND a + b + c = 1000 AND a < b < c (or False if not)."""
    return ((a**2 + b**2) == c**2) and (a + b + c == 1000) and (a < b < c)


def findPyth(maxNum):
    """Returns the final product abc if a, b, and c are Special Pythagorean Triplets"""
    for a in range(1,maxNum):
        for b in range(1,maxNum):
            for c in range(1,maxNum):
                if isPythagoreanTriplet(a,b,c):
                    print "Found it!"
                    print "a: " + str(a) + ", b: " + str(b) + ", c: " + str(c)
                    finalProduct = a*b*c                    
                    return finalProduct

    
startTime = time.time()

maxNum = 500

finalProduct = findPyth(maxNum)

print "abc = " + str(finalProduct)

print "Time Elapsed: " + str(time.time() - startTime)
