#Problem 3 from projecteuler.net
#Author: Blair Gemmer
"""Description of Problem 3, Largest prime factor:

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import csv, math, os

def isprime(n):
    #make sure n is a positive integer
    n = abs(int(n))
    #0 and 1 are not primes
    if n < 2:
        return False
    #2 is the only even prime number
    if n == 2:
        return True
    #all other even numbers are not primes
    if not n & 1:
        return False
    #range starts with 3 and only needs to go up to the square root of n
    #for all odd numbers
    for x in range (3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True #if it makes it through all the catches, it is a prime

#To create prime number csv file:
def createPrimesFile():
    if os.path.exists("Resources//primenumbers.csv") == False:
        with open("Resources//primenumbers.csv", 'wb') as f:
            writer = csv.writer(f, delimiter=',')
            tempList = []    
            for i in range(2, 104730):                        
                if isprime(i):
                    tempList.append(i)
                if len(tempList) == 10: #10 items per row
                    writer.writerow(tempList)
                    tempList = []
    else:
        print "File already exists."
        
#To check isprime function:
def checkprimefunction(isPrime):
    primes = []

    with open("Resources//primenumbers.csv") as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            for item in row:
                primes.append(item)


    for primeNumber in primes:
        result = isPrime(primeNumber)
        if result == True:
            pass
        else:
            print "The isprime function does not work properly."
            return False
    print "The isprime function works properly on the first 10,000 primes"
    return True

#Finds the largest prime factor of any given n (using the sieve of Eratosthenes):
def findLargestPrimeFactor(n):
    maxNumber = -1;
    #range only needs to go up to the square root of n
    for x in xrange(2, n/2):        
        if (isprime(x) and n % x == 0):
            maxNumber = x
    return maxNumber

#n = 600851475143

#print findLargestPrimeFactor(n)

def findLargestPrimeFactor(n):
    primes = []
    with open("Resources//primenumbers.csv") as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            for item in row:
                primes.append(item)

        for primeNumber in primes:
            if n % int(primeNumber) == 0:
                print primeNumber

n = 600851475143
print findLargestPrimeFactor(n)
