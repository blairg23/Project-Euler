# -*- coding: utf-8 -*-
#Problem 453 from projecteuler.net
#Author: Blair Gemmer

"""Description of Problem 453, Lattice Quadrilaterals:
A simple quadrilateral is a polygon that has four distinct vertices, has no straight angles and does not self-intersect.

Let Q(m, n) be the number of simple quadrilaterals whose vertices are lattice points with coordinates (x,y) satisfying 0 ≤ x ≤ m and 0 ≤ y ≤ n.

For example, Q(2, 2) = 94 as can be seen here:

            http://projecteuler.net/project/images/p453_quad.png

It can also be verified that Q(3, 7) = 39590, Q(12, 3) = 309000 and Q(123, 45) = 70542215894646.

Find Q(12345, 6789) mod 135707531.
"""

import math, itertools
import numpy as np
import matplotlib.pyplot as plt

testing = False


def createMesh(width, height):
    """Returns a mesh consisting of every point within width and height, including the origin (0,0)"""
    mesh = [(x,y) for x in range(0, width+1) for y in range(0,height+1)]
    return mesh

def distance(a,b):
    """Returns the distance between point a and b"""    
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def is_on(a, b, c):
    """Returns true iff point c intersects the line segment from a to b"""
    return(isCollinear(a, b, c) and (within(a[0], c[0], b[0]) if a[0] != b[0] else
                                     within(a[1], c[1], b[1])))

def slope(a, b):
    """Returns the value of the slope between point a and b"""
    if a[0] == b[0]: #If the x values are both 0
        return 0 #Technically, undefined, but doesn't matter for finding collinearity
    return (a[1] - b[1]) / (a[0] - b[0])

def isCollinear(a,b,c):
    """Returns True if the three points are collinear, False if not"""
    #return slope(a, b) == slope(b, c) == slope(c, a) #DOES NOT WORK
    #return (b[0] - a[0]) * (c[1] - a[1]) == (c[0] - a[0]) * (b[1] - a[1]) 
    #return distance(a,b) + distance(b,c) == distance(a,c)
    x1 = a[0]
    y1 = a[1]
    x2 = b[0]
    y2 = b[1]
    x3 = c[0]
    y3 = c[1]    
    if (x1*(y2 - y3)) + (x2*(y3 - y1)) + (x3*(y1-y2)) == 0:      
        return True
    else:
        return False
    
def within(p, q, r):
    """Returns true iff q is between p and r (inclusive)."""
    return p <= q <= r or r <= q <= p

def hasCollinearPoints(listOfPoints):
    """Returns True if the list of points contains collinear points, False if not"""
    for points in listOfPoints:
        if isCollinear(points[0], points[1], points[2]): #If any of the points are collinear
            return True
        else:
            pass
    return False #If none of the points are collinear


def Q(m, n):
    """Returns the number of simple quadrilaterals who vertices are lattice points with coordinates (x, y)
    such that 0 <= x <= m and 0 <= y <= n.
    """
    width = m
    height = n
    mesh = createMesh(width, height)
    print "Mesh: " + str(mesh)
    
    allCombs = [x for x in itertools.combinations(mesh, 4)] #Holds all combinations of points for the mesh
    nonLinearCombs = [] #Will hold the non-linear combinations of that mesh

    for i in range(len(allCombs)):
        #Takes each set of 4 points and creates all combinations of 3 individual points, to check collinearity:
        indComb = [x for x in itertools.combinations(allCombs[i], 3)]
        if hasCollinearPoints(indComb) == False:
            nonLinearCombs.append(allCombs[i])
    print len(nonLinearCombs)
Q(123,45)

#Testing purposes (to see if collinearity is being checked correctly):
if testing:
    #Checks all combinations in a sample mesh:
    width = 2
    height = 2
    sampleMesh = createMesh(width, height)
    print "Sample Mesh: " + str(sampleMesh)

    allCombs = [x for x in itertools.combinations(sampleMesh, 4)] #Holds all combinations of points for the mesh
    nonLinearCombs = [] #Will hold the non-linear combinations of that mesh

    print 'Combinations without replacement:'
    for i in range(len(allCombs)):
        #Takes each set of 4 points and creates all combinations of 3 individual points, to check collinearity:
        indComb = [x for x in itertools.combinations(allCombs[i], 3)]
        if hasCollinearPoints(indComb) == False:
            print allCombs[i], i
            
    #Plots those combinations into a scatter plot so you can visually see if the quadrilateral has collinear points:            
    i = 16
    indComb = [x for x in itertools.combinations(allCombs[i], 3)]
    hasCollinearPoints(indComb)
    print allCombs[i]
    if hasCollinearPoints(indComb) == False: #If you want to show the points that are NOT collinear, set to False. Set to True otherwise.
        x = [p[0] for p in allCombs[i]]
        y = [p[1] for p in allCombs[i]]
        print x,y
        plt.scatter(x, y)
        plt.show()        




##combsr = [x for x in itertools.combinations_with_replacement(sampleMesh, 4)]
##print 'Combinations with replacement:'
##for i in combsr:
##    print i
##print len(combsr)


##combs = [zip(x, list2) for x in itertools.combinations(list1, 4)]
##print 'Combinations without replacement:'
##for i in combs:
##    print i
##
##combsr = [zip(x, list2) for x in itertools.combinations_with_replacement(list1, 4)]
##print 'Combinations with replacement:'
##for i in combsr:
##    print i
##
##perms = [zip(x, list2) for x in itertools.permutations(list1, 4)]
##
##print 'Permutations:'
##for i in perms:
##    print i
##
