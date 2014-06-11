# -*- coding: utf-8 -*-
#Problem 17 from projecteuler.net
#Author: Blair Gemmer

"""Description of Problem 17, Number letter counts:
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
"""


def getOnes(n):
    """Returns the British word for the number n"""    
    if n == 1:
        return "one"
    elif n == 2:
        return "two"
    elif n == 3:
        return "three"
    elif n == 4:
        return "four"
    elif n == 5:
        return "five"
    elif n == 6:
        return "six"
    elif n == 7:
        return "seven"
    elif n == 8:
        return "eight"
    elif n == 9:
        return "nine"
    elif n == 0:
        return ""
    else:
        return "no one knows this number"
def getTensIfOne(n):
    """Returns the British word for the number n, in tens terms, if the number is 1"""
    if n == 10:
        return "ten"
    elif n == 11:
        return "eleven"
    elif n == 12:
        return "twelve"
    elif n == 13:
        return "thirteen"
    elif n == 14:
        return "fourteen"
    elif n == 15:
        return "fifteen"
    elif n == 16:
        return "sixteen"
    elif n == 17:
        return "seventeen"
    elif n == 18:
        return "eighteen"
    elif n == 19:
        return "nineteen"
    elif n == 00:
        return ""
    else:
        return "No one knows this number"
def getTens(n):
    """Returns the British word for the number n, in tens terms"""
    if n == 2:
        return "twenty"
    elif n == 3:
        return "thirty"
    elif n == 4:
        return "forty"
    elif n == 5:
        return "fifty"
    elif n == 6:
        return "sixty"
    elif n == 7:
        return "seventy"
    elif n == 8:
        return "eighty"
    elif n == 9:
        return "ninety"
    elif n == 0:
        return ""
    else:
        return "no one knows this number"
def getHundreds(n):
    """Returns the British word for the number n, in hundreds terms"""
    if n == 1:
        return "onehundred"
    elif n == 2:
        return "twohundred"
    elif n == 3:
        return "threehundred"
    elif n == 4:
        return "fourhundred"
    elif n == 5:
        return "fivehundred"
    elif n == 6:
        return "sixhundred"
    elif n == 7:
        return "sevenhundred"
    elif n == 8:
        return "eighthundred"
    elif n == 9:
        return "ninehundred"
    else:
        return "no one knows this number"

def getThousands(n):
    """Returns the British word for the number n, in thousands terms"""
    if n == 1:
        return "onethousand"
    elif n == 2:
        return "twothousand"
    elif n == 3:
        return "threethousand"
    elif n == 4:
        return "fourthousand"
    elif n == 5:
        return "fivethousand"
    elif n == 6:
        return "sixthousand"
    elif n == 7:
        return "seventhousand"
    elif n == 8:
        return "eightthousand"
    elif n == 9:
        return "ninethousand"
    else:
        return "no one knows this number"

def returnBritish(n):
    num = str(n)
    length = len(num)
    if length == 1:
        return getOnes(n)
    elif length == 2:
        if num[0] == "1":
            return getTensIfOne(int(num[0]+num[1]))
        else:
            return getTens(int(num[0])) + getOnes(int(num[1]))
    elif length == 3:
        if num[1] == "1":
            return getHundreds(int(num[0]))+ "and" + getTensIfOne(int(num[1]+num[2]))
        elif num[1] == "0":
            if num[2] == "0":
                return getHundreds(int(num[0]))
            else:
                return getHundreds(int(num[0])) + "and" + getOnes(int(num[2]))
        else:
            return getHundreds(int(num[0])) + "and" + getTens(int(num[1])) + getOnes(int(num[2]))
    elif length == 4:
        if num[1] == "0":
            if num[2] == "1":
                return getThousands(int(num[0])) + "and" + getTensIfOne(int(num[2]+num[3]))
            elif num[2] == "0":
                if num[3] == "0":
                    return getThousands(int(num[0]))
                else:
                    return getThousands(int(num[0])) + "and" + getOnes(int(num[3]))
            else:
                if num[3] == "0":
                    return getThousands(int(num[0]))
                else:
                    return getThousands(int(num[0])) + "and" + getOnes(int(num[3]))
        else:
            if num[2] == "1":
                return getThousands(int(num[0])) + "and" + getHundreds(int(num[1])) + "and" + getTensIfOne(int(num[2]+num[3]))
            elif num[2] == "0":
                if num[3] == "0":
                    return getThousands(int(num[0])) + "and" + getHundreds(int(num[1]))
                else:
                    return getThousands(int(num[0])) + "and" + getHundreds(int(num[1])) + "and" + getOnes(int(num[3]))
            else:
                return getThousands(int(num[0])) + "and" + getHundreds(int(num[1])) + "and" + getTens(int(num[2])) + getOnes(int(num[3]))
    else:
        return "MAJOR MALFUNCTION!"

britNumbers = []
for n in range(0,1001):
    britNumbers.append(returnBritish(n))

sumOfLetters = 0
for n in britNumbers:
    sumOfLetters += len(n)

print sumOfLetters
