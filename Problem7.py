#Problem 7 from projecteuler.net
#Author: Blair Gemmer

"""Description of Problem 7, 10001st prime:
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

Side Note: I'll be utilizing the prime numbers we fetched from Problem 3.
"""

import csv
from Problem3Solution2 import *

primes = []

with open("Resources//primenumbers.csv") as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        for item in row:
            primes.append(item)

print primes[9999] #The 10,000th prime

ttPrime = int(primes[9999])
offset = 100 #Try first n numbers after the 10,000th prime
for i in range(ttPrime+1, ttPrime + offset):
    if IsNumberPrime(i):
        print "The 10,001st prime number is: " + str(i)
        break
