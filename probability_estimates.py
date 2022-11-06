#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import percolation_rectangular as pr
import percolation_triangular as pt

def F(n,p,trials):  
    """function that finds the probablity if there exists a yellow path for many trials."""
    count = 0                               
    for i in range(trials):                 
        if pr.path_exist(pr.randomgrid(n,p)):
            count += 1
    
    return count/trials

def F_efficient(n,p,trials):
    """A simple function which estimates the probability that there is a yellow path connecting the left and right 
    sides of an n-by-n grid with probability p."""
    count = 0                                  # We count the number of grids in our trials with a yellow path 
    for i in range(trials):                    # connecting the left and right sides. 
        if pr.path_exist_efficient(pr.randomgrid(n,p)):
            count += 1
    return count/trials

def F_rect(n,m,p,trials):
    """A simple function which estimates the probability that there is a yellow path connecting the left and right 
    sides of an n-by-m grid with probability p."""
    count = 0                                  # We count the number of grids in our trials with a yellow path 
    for i in range(trials):                    # connecting the left and right sides. 
        if pr.path_exist_efficient(pr.randomgridrect(n,m,p)):
            count += 1
    return count/trials

def G(n,p,trials):
    count = 0
    for i in range(trials):
        if pr.path_exist_from_center(pr.randomgrid(n,p)):
            count += 1
    
    return count/trials

def F_tri(n,p,trials):
    count = 0
    for i in range(trials):
        if pt.path_exist_triangular(pr.randomgrid(n,p)):
            count += 1
    
    return count/trials

def T_equilateral(n, p, trials):
    count = 0

    for i in range(trials):
        points = pt.random_triangular_lattice(n,p)
        X=points[1]
        if pt.path_exist_from_base(X,0.2):
            count += 1
    
    return count/trials