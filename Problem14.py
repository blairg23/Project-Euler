# -*- coding: utf-8 -*-
#Problem 14 from projecteuler.net
#Author: Blair Gemmer

"""Description of Problem 14, Longest Collatz sequence:
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

ANSWER (In case you don't want to run the program):
Max Length so far: 525
Current Winner so far: 837799
Time Elapsed: 109.286999941
Final winner: 837799
"""

import time, os

testing = True

chains = {} #Keep track of the chains with a dictionary

def createChain(chain):
    n = chain[len(chain)-1]
    if n == 1: #If we're at the end of the list        
        return chain, len(chain) #Return the chain and its length
    if n % 2 == 0: #If we're dealing with an even number:
        n = n / 2
        chain.append(n)
        return createChain(chain)
    else: #Otherwise, if we're dealing with an odd number:
        n = (3 * n) + 1
        chain.append(n)
        return createChain(chain)

if testing:
    startNum = 13
    chain = [startNum]
    chain = createChain(chain)
    print "Chain created by the number " + str(startNum) + " is " + str(chain[0])
    print "Its length is " + str(chain[1]) + "."
        
        
maxLength = -1
currentWinner = ""
clear = "\n" * 100
start = time.time()
for i in range(1, 1000000): #Under 1 million
    chain = [i]
    chain = createChain(chain)
    if chain[1] > maxLength: #If the length of the current chain is bigger than our max
        maxLength = chain[1] #Change max length to the new current chain length
        currentWinner = i    #This is our current best number (with the longest chain)
        print clear
        print "Max Length so far: " + str(maxLength)
        print "Current Winner so far: " + str(currentWinner)
        print "Time Elapsed: " + str(time.time() - start)
print "Final winner: " + str(currentWinner)
