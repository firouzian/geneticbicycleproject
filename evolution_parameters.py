# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 00:38:56 2017

@author: user-guest
"""
#lalalala

class Evolution_Parameters(object):
    """Parameters set by the User in relation to the evolutionary process"""
    def __init__(self,merge_range,mutability,num_genes,num_generations):
        # Range in wich new generation can ecxeed the parents parameters
        self.merge_range = merge_range 
        # Chance of mutation
        self.mutability = mutability
        # Total number of bicycles (genes) in each generation
        self.num_genes = num_genes
        # Number of generation we want to evolve
        self.num_generations = num_generations