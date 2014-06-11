#Problem 10 from projecteuler.net
#Author: Blair Gemmer

"""Description of Problem 10, Summation of primes:

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

Side note: Again, I'll utilize the list of primes I created in Problem 3
"""

from Problem3Solution2 import *
import time, csv

startTime = time.time()
primes = []

with open("Resources//primenumbers.csv") as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        for item in row:
            primes.append(int(item))


for i in range(int(primes[len(primes)-1])+1, 2000000): #Primes we haven't found yet that are less than 2 million
    if IsNumberPrime(i):
        primes.append(int(i))
        

print len(primes) - 10000
print "The sum of the primes less than 2 million is: " + str(sum(primes))
print "Time elapsed: " + str(time.time() - startTime)
