#Problem 5 from projecteuler.net
#Author: Blair Gemmer
"""Description of Problem 5, Smallest multiple:
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

from fractions import gcd
import inspect
import time

def gcd2(a, b):
    """Returns greatest common divisor of two integers using Euclid's Algorithm"""
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Returns the least common multiple of two integers"""
    return abs(a * b) // gcd(a, b)

def lcmm(*args):
    """Returns the lcm of args."""
    return reduce(lcm, args)


start = time.time()
n = 20

numList = [x for x in range(1, n+1)]

print "Method 1:------------------"
print "Least common multiple is: " + str(lcmm(*numList))

elapsed = time.time() - start
print "And took : " + str(elapsed) + " seconds to complete."

print ""
def lcm(x,y):
    tmp=x
    while (tmp%y)!=0:
        tmp+=x
    return tmp

def lcmm(*args):
    return reduce(lcm,args)

start = time.time()
n = 20
start = time.time()
args = [x for x in range(1, n+1)]

print "Method 2:------------------"
print "Least common multiple is: " + str(lcmm(*args))
elapsed = time.time() - start
print "And took : " + str(elapsed) + " seconds to complete."
