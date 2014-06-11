# -*- coding: utf-8 -*-
#Problem 25 from projecteuler.net
#Author: Blair Gemmer

"""Description of Problem 25, 1000-digit Fibonacci number:
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000 digits?
"""
from math import sqrt

def Fib(n):
    """Returns the nth Fibonacci number from the sequence"""
    return long(((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5)))

def F():
    """Yields the Fibonacci sequence as an iterator. Don't forget to break or use a subset of the sequence."""
    a,b = 0,1
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b

def SubFib(startNumber, endNumber):
    """Yields the Fibonacci sequence between startNumber and endNumber."""
    for cur in F():
        if cur > endNumber: return
        if cur >= startNumber:
            yield cur

finalNumber = 0
counter = 0
for f in F():
    if len(str(f)) == 1000:
        finalNumber = f
        finalCount = counter
        break
    counter += 1

print finalNumber
print "Counter: " + str(counter)

