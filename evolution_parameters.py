# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 00:38:56 2017

@author: user-guest
"""
#lalalala

class Evolution_Parameters(object):
    """Parameters set by the User in relation to the evolutionary process"""
    def __init__(self,merge_range,mutability,num_genes,num_generations):
        self.merge_range = merge_range
        self.mutability = mutability
        self.num_genes = num_genes
        self.num_generations = num_generations