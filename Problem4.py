#Problem 4 from projecteuler.net
#Author: Blair Gemmer
"""Description of Problem 4, Largest palindrome product:
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

testing = False

def isPalindrome(n):
    """Returns True if the number is a palindrome and False if it is not"""
    n = str(n)
    size = len(n)
    if testing:
        print "Is " + n + " a palindrome? It has size = " + str(size) + "."
    if size == 2 and n[0] != n[1]:
        if testing:
            print "False, because " + str(n[0]) + " != " + str(n[1]) + "."
            print ""
        return False
    for i in range(size):
        if n[i] == n[size-i-1]:
            if testing:                
                print str(n[i]) + " = " + str(n[size-i-1])
            pass
        else:
            if testing:
                print "False, because " + str(n[i]) + " != " + str(n[size-i-1])
                print ""
            return False        
    if testing:
        print "True, because everything matched up."
        print ""
    return True

if testing:
    n = 10101
    isPalindrome(n)

    n = 10010
    isPalindrome(n)


start = 100
end = 1000
maxPal = -1
for x in range(start,end):
    for y in range(start,end):
        result = x*y
        if isPalindrome(result):
            if result > maxPal:
                maxPal = result

print maxPal                
                
