#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
from random import *

def randomgrid(n,p):  
    """Generates an n by n grid with each element 1 with probability p and 0 with probability 1-p.
    The output is in the form of a numpy array."""
    X = np.zeros((n,n))                        # We start with an n by n numpy array of zeros.
    for i in range(n):
        for j in range(n):                     # These two for loops span through every element of the array.
            if random() < p:                   # random() generates a random float uniformly between 0 and 1,
                X[i][j] = 1                    # hence the probability that random() < p is p as desired.
    return X

def randomgridrect(n,m,p):
    """Generates an n by m grid with each element 1 with probability p and 0 with probability 1-p.
    The output is in the form of a numpy array."""
    X = np.zeros((n,m))                        # We start with an n by m numpy array of zeros.
    for i in range(n):
        for j in range(m):                     # These two for loops span through every element of the array.
            if random() < p:                   # random() generates a random float uniformly between 0 and 1,
                X[i][j] = 1                    # hence the probability that random() < p is p as desired.
    return X

def get_adjacent_indices(i, j, n, m):  ##q2
    """A function whith inputs i, j the coordinates of a site in our grid and n, m the shape of our grid, and 
    outputs the coordinates of the adjacent sites."""
    # These if statements deal with the cases that our site is on any of the boundaries of our grid.
    adjacent_indices = []
    if i > 0:
        adjacent_indices.append((i-1,j))
    if i+1 < n:
        adjacent_indices.append((i+1,j))
    if j > 0:
        adjacent_indices.append((i,j-1))
    if j+1 < m:
        adjacent_indices.append((i,j+1))
    return adjacent_indices

def total(X):
    """A simple function which gives the total of all sites in a given grid."""
    total = 0
    (n,m) = np.shape(X)
    for i in range(n):
        for j in range(m):
            total += X[i][j]
    return total

def path_exist(X):
    """A function which given a grid will find all reachable sites and assign them a value of 0.5. If there is a 
    yellow path connecting the left and right sides of the grid it outputs True, else it outputs False."""
    (n,m) = np.shape(X)
    for i in range(n):
        if X[i][0] > 0:
            X[i][0] = 2                        # We start by setting all yellow sites on the left edge as reachable.
    
    step = 2
    # The use of step ensures that each reachable site is only tested once for adjacent yellow sites, which are
    # subsequently marked as reachable.
    while True:                                # This starts a loop which will run forever unless we use break.
        initial = total(X)                     # We use the total to test if the step has found any new reachable
        for j in range(m):                     # sites.
            for i in range(n):
                if X[i][j] == step:
                    for (u,v) in get_adjacent_indices(i,j,n,m):
                        if X[u][v] == 1:
                            X[u][v] = step+1
        step += 1
        if total(X) == initial:                # If no new reachable sites are found after the previous step we
            break                              # break our while loop, stopping the search for more reachable sites.
    
    for i in range(n):                         # This sets any site found to be reachable a value of 0.5.
        for j in range(m):
            if X[i][j] > 1:
                X[i][j] = 0.5
    
    path_found = False                         # We start by setting path_found to False, then we run through the
    for i in range(n):                         # sites of the right edge checking if they are reachable, if so we
        if X[i][m-1] == 0.5:                   # set path _found to True.
            path_found = True

    return path_found

def path_exist_efficient(X):
    """A more efficient function of the function above, which runs as quickly as possible, which given a grid will 
    find all reachable sites and assign them a value of 0.5. If there is a yellow path connecting the left and
    right sides of the grid it outputs True, else it outputs False."""
    n,m = np.shape(X)  #np.shape: to find dimensions of the matrix
    path_found = False #setting the initial statement of the path_found flag as false
    reachable = []     #define an empy list of reachables

    for i in range(n): #This runs through all the sites on the left edge, setting them as reachable (0.5)
                       #if they are yellow (1)
        if X[i,0]==1:  
            X[i,0]=0.5 
            reachable.append((i,0))
            
    count = 0 #setting the initial count as zero
    
    while count <= (len(reachable)-1): #We loop until we have checked all the elements in the reachable list
        row,col = reachable[count] 
        adj_ind = get_adjacent_indices(row,col,n,m)
        
        for indice in adj_ind:
            a,b = indice
            if X[a,b] ==1: #if there is an adjacent site which is yellow (1) set is as red (0.5)
                X[a,b]=0.5
                reachable.append(indice) 
                if b== m-1: #if the site is on the right edge, there is a path found and we return true
                    return True
        count += 1
        
    return path_found

def path_exist_from_center(X):
    """This function determines if there is a path from the center of the grid to the boundary"""
    n,m = np.shape(X)       #get numbers of row and col of X and initialise 
    path_found=False        
    reachable = []
    
    row = int((n+1)/2)      #If center site is yellow, mark as reachable otherwise return False
    col = int((m+1)/2)
    if X[row,col] == 1:
        X[row, col] = 0.5
        reachable.append((row,col))
    else:
        return False

    count = 0
    while count <= (len(reachable)-1):           #Loop until wehace checked all the reachable sites
        row,col = reachable[count]               #Get next site in the list and find adjacent indices
        adj_ind = get_adjacent_indices(row,col,n,m)
        
        for indice in adj_ind:
            a,b = indice
            if X[a,b] ==1:   #if site is yellow, mark as reachable
                X[a,b]=0.5
                reachable.append(indice) 
                if b== m-1 or b==0 or a==0 or a==n-1:  #if site is on the boundary, return True
                    return True
        count +=1
        
    return path_found #if we do not find a reachable site on the boundary, return False

