#Problem 3 in projecteuler.net
#Another solution, without using a csv list of prime numbers
"""Description of Problem 3, Largest prime factor:

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import math

def IsNumberPrime(n):
   bounds = int(math.sqrt(n))
   for number in xrange(2,bounds+2):
        if n % number == 0:
            return False
   return True

def GetListOfFactors(n):
   factors = []
   bounds = int(math.sqrt(n))
   startNo = 2

   while startNo <= bounds:
      if n % startNo == 0:
         factors.append(startNo)
      startNo += 1
   return factors

def GetListOfPrimeFactors(n):
    primes = []
    factors = GetListOfFactors(n)
    if n % 2 == 0:
       primes.append(2)

    for entries in factors:
       if IsNumberPrime(entries):
          primes.append(entries)
    return primes


primes = GetListOfPrimeFactors(600851475143)

print primes
