#Problem 1 from projecteuler.net
#Author: Blair Gemmer
"""Description of Problem 1, Multiples of 3 or 5:
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

n = 1000
multiples = []

for i in range(0,n):
    if (i % 3 == 0 or i % 5 == 0):
        multiples.append(i)

print sum(multiples)        
