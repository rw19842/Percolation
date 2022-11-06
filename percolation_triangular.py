#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
from random import *
import percolation_rectangular as pr
import matplotlib.pyplot as plt
from matplotlib import colors

colours = colors.ListedColormap(["blue","red","yellow"])

def get_adjacent_indices_triangular(i, j, n, m):  
    """A function with inputs i, j the coordinates of a site in our grid and n, m the shape of our grid, and 
    outputs the coordinates of the adjacent sites, including diagonals of the form x + (1,1)."""
    adjacent_indices = []
    if i > 0:
        adjacent_indices.append((i-1,j))
    if i+1 < n  and (i+1)<=j:
        adjacent_indices.append((i+1,j))
    if j > 0 and i <= (j-1):
        adjacent_indices.append((i,j-1))
    if j+1 < m:
        adjacent_indices.append((i,j+1))
    if i<=n-2 and j<=n-2:
        adjacent_indices.append((i+1,j+1))
    if i<0 and j<0:
        adjacent_indices.append((i-1,j-1))
    return adjacent_indices

def path_exist_triangular(X):
    """A function which takes as input a square grid, but only considers the triangle with its right angle in the bottom right corner """
    """where adjacent sites are as described above, this is analagous to a triangular lattice"""
    """This function attempts to find a path from the bottom left corner of the grid to the right edge."""
    
    n,m = np.shape(X)                            #we get the shape of the grid and initialise our variables
    path_found = False
    reachable = []
    
    if X[0,0]==1:                                #If the bottom left corner is yellow then we mark it as reachable
        X[0,0]=0.5
        reachable.append((0,0))
    else: return path_found                       #Otherwise we return False

    count = 0

    while count <= (len(reachable)-1):           #We loop until we have checked all reachable indices
        row,col = reachable[count]               #Look at next reachable element and fetch the indices of adjacent sites
        adj_ind = get_adjacent_indices_triangular(row,col,n,m)
        
        for indice in adj_ind:                   
            a,b = indice
            if X[a,b] ==1:                       #If an adjacent site is yellow, mark as reachable
                X[a,b]=0.5
                reachable.append(indice) 
                if b== m-1:                      #If a reachable site is on the right edge of the grid, we return True
                    return True
        count +=1
        
    return path_found                            #If no reachable site is on the right edge, return False

def triangular_position(i,j):
    """This simple function transforms takes as input the indice of a site and returns the (x,y) co-ordinates of the site"""
    """as part of a triangular lattice on a pair of axes"""
    return (j-i/2, (3**0.5)*i/2)

def random_triangular_lattice(size,p):
    """This creates a randomgrid similar to the square and another matrix containing the (x,y) co-ordinates"""
    """of the sites in the triangular lattice and returns a list containing both matrices"""
    X= pr.randomgrid(size, p)                        
    Y= np.empty((size,size), dtype = object)

    for i in range(size):
        for j in range(size):
            Y[i,j] = triangular_position(i,j)
            
    points = [Y,X]
    return points

def print_equilateral_triangle(lattice):
    """Takes as input a list of two matrices as created in random_triangular_lattice and prints the right angled triangle"""
    """we consider in path_exist_triangular as an equilateral triangle lattice on a pair of axes"""

    Y=lattice[0]
    X=lattice[1]
    row, col = np.shape(X)    
    points = [[],[]]
    for i in range(col):                     #We create two lists, taking only the information for the right angled triangle in the grid  
        for j in range(i+1):
            points[0].append(Y[j,i])
            points[1].append(X[j,i])
                
    
    #Now we plot the a scatter graph of all these points, using the same colour scheme as in random grid 
    plt.scatter(*zip(*points[0]), c=points[1], cmap = colours)
    
    plt.axis('square')

def path_exist_from_base(X, r):
    """This function checks if the base of the triangle is connected by a yellow path to the right"""
    """side within distance rn of the top vertex, where n is the length of the sides of the triangles"""
    """by looking at the right angled triangle in the grid"""
    n,m = np.shape(X)                         #we get the shape of X and initialise our variables
    path_found = False
    reachable = []
    
    for j in range(m):                        #Looking along the base and setting any yellow sites to reachable
        if X[0,j]==1:
            X[0,j] = 0.5
            reachable.append((0,j))
    count = 0

    while count <= (len(reachable)-1):        #Loop until there are no elements left in the list
        row,col = reachable[count]            #Look at next reachable element and fetch the indices of adjacent sites
        adj_ind = get_adjacent_indices_triangular(row,col,n,m)
        
        for indice in adj_ind:                
            a,b = indice
            if X[a,b] == 1:                   #If adjacent indice is yellow, mark as reachable
                X[a,b]=0.5
                reachable.append(indice) 
                if a >= int(n*(1-r)) and b==m-1: #if site is on the right side within distance rn of the top vertex, return True
                    return True
        count +=1
        
    return path_found  #If no reachable sites as described are found, return false
