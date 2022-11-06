#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np

def random_grid_soph(n,m):
    """This creates an n-by-m grid, with each site assigned an independent Uniform[0,1] random variable."""
    return np.random.rand(n,m)

def minimum_p(X, path_function):
    """This function, given a grid from random_grid_soph and a path_function finds the minimum p for which there is 
    a path of sites with value less than p."""
    n,m = np.shape(X)
    
    plist = [i/1000 for i in range(1000)]      # Creating a list of p values.
 
    for p in range(len(plist)):                # We run through all our p-values setting each of our sites in Y to
        Y = np.zeros((n,m))                    # 1 (yellow) corresponding to a site in X with a value less than p.
        for i in range(n):
            for j in range(m):
                if X[i][j] <= plist[p]:
                    Y[i][j] = 1
                    
        if path_function(Y):                   # If there is a path in Y we return the value of p for which we found
            return plist[p]                    # this path.
    return 1 

def critical_point(n,m,trials,path_function):
    """This function estimates the critical point of an n-by-m grid of a given path_function."""
    pc = 0
    # We run our function minimum_p multiple times to get an estimate of the critical point.
    for i in range(trials):
        pc += minimum_p(random_grid_soph(n,m),path_function)
    return pc/trials
