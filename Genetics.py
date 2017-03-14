#!/usr/bin/python

# Genetic part of Genetic Bicycle project
import numpy as np
import scipy as sp
import random as rd
from gene import Gene
from user_parameters import User_Parameters

# Defines a function that creates a list of n random genes
#   Those genes are restrected some ranges defined by the user
def Create_Genelist(EP,UP):
    '''
    Create a list of Random Genes.
    '''
    GL=[]
    for i in range(EP.num_genes):
        rand_M1_x=rd.uniform(UP.x_min,UP.x_max)
        rand_M1_y=rd.uniform(UP.y_min,UP.y_max)
        rand_M2_x=rd.uniform(UP.x_min,UP.x_max)
        rand_M2_y=rd.uniform(UP.y_min,UP.y_max)
        rand_W1_x=rd.uniform(UP.x_min,UP.x_max)
        rand_W1_y=rd.uniform(UP.y_min,UP.y_max)
        rand_W2_x=rd.uniform(UP.x_min,UP.x_max)
        rand_W2_y=rd.uniform(UP.y_min,UP.y_max)
        SC=rd.uniform(0,UP.SC_max)
        d=0
        GL.append(Gene(rand_M1_x,rand_M1_y,rand_M2_x,rand_M2_y,rand_W1_x,rand_W1_y,rand_W2_x,rand_W2_y,SC,d))            
    return GL
    
    
def Evolve_Genes(genelist,EP,UP):
    '''
    Evolves a genelist into a new generation based on fitness score d.
    '''
    new_genelist=[]
    d_sum=0
    
    # Gets the overall fitness of the entire genelist for then choose parents based on this
    for gen in genelist:
        d_sum+=gen.d
    
    # --------Selecting Parents for each member of the new generation----------

    for i in range(len(genelist)):
        r=rd.uniform(0,d_sum)
        temp_sum=0
        j=0
        
        # The chance of being selected is the fitness of the gene [d] divided the total sum [d_sum]
        while (temp_sum<r):
            parent_1=j            
            temp_sum+=genelist[j].d
            j+=1
            
        # Repeat all the procces to select second parent, but not allowing to select the same gene again      
        parent_2=parent_1 # Set this to enter the while loop
        while parent_1 == parent_2: # Leaves the loop when the new gene has to differents parents
            r=rd.uniform(0,d_sum)
            temp_sum=0
            j=0
            while (temp_sum<r):
                parent_2=j            
                temp_sum+=genelist[j].d
                j+=1           
                
        # ------------Merging the genes to make new generation.----------------
                
        # Each new parameter is choosen in a range determined by the parameters of their parents.
        # The reange is set by the evolution parameters 
                # (must excede the limits of the parents to prevent shrinking in the parameter space)
        
        max_val = max(genelist[parent_1].M1_x,genelist[parent_2].M1_x)
        min_val = min(genelist[parent_1].M1_x,genelist[parent_2].M1_x)
        extra=(max_val-min_val)*(EP.merge_range)
        new_M1_x=rd.uniform(min_val-extra,max_val+extra)
        # Now we roll the dice of mutation
        if (rd.uniform(0,1)<EP.mutability):
            # If works, we move a random amount around the previos value
            new_M1_x+=rd.uniform(UP.x_min,UP.x_max)-(0.5*abs(UP.x_max-UP.x_min))
        
        # --------Repeat the same process for all the parameters---------------
        
        max_val = max(genelist[parent_1].M1_y,genelist[parent_2].M1_y)
        min_val = min(genelist[parent_1].M1_y,genelist[parent_2].M1_y)
        extra=(max_val-min_val)*(EP.merge_range)
        new_M1_y=rd.uniform(min_val-extra,max_val+extra)
        if (rd.uniform(0,1)<EP.mutability):
            new_M1_y+=rd.uniform(UP.y_min,UP.y_max)-(0.5*abs(UP.y_max-UP.y_min))

        max_val = max(genelist[parent_1].M2_x,genelist[parent_2].M2_x)
        min_val = min(genelist[parent_1].M2_x,genelist[parent_2].M2_x)
        extra=(max_val-min_val)*(EP.merge_range)
        new_M2_x=rd.uniform(min_val-extra,max_val+extra)
        if (rd.uniform(0,1)<EP.mutability):
            new_M2_x+=rd.uniform(UP.x_min,UP.x_max)-(0.5*abs(UP.x_max-UP.x_min))
        
        max_val = max(genelist[parent_1].M2_y,genelist[parent_2].M2_y)
        min_val = min(genelist[parent_1].M2_y,genelist[parent_2].M2_y)
        extra=(max_val-min_val)*(EP.merge_range)
        new_M2_y=rd.uniform(min_val-extra,max_val+extra)
        if (rd.uniform(0,1)<EP.mutability):
            new_M2_y+=rd.uniform(UP.y_min,UP.y_max)-(0.5*abs(UP.y_max-UP.y_min))

        max_val = max(genelist[parent_1].W1_x,genelist[parent_2].W1_x)
        min_val = min(genelist[parent_1].W1_x,genelist[parent_2].W1_x)
        extra=(max_val-min_val)*(EP.merge_range)
        new_W1_x=rd.uniform(min_val-extra,max_val+extra)
        if (rd.uniform(0,1)<EP.mutability):
            new_W1_x+=rd.uniform(UP.x_min,UP.x_max)-(0.5*abs(UP.x_max-UP.x_min))
        
        max_val = max(genelist[parent_1].W1_y,genelist[parent_2].W1_y)
        min_val = min(genelist[parent_1].W1_y,genelist[parent_2].W1_y)
        extra=(max_val-min_val)*(EP.merge_range)
        new_W1_y=rd.uniform(min_val-extra,max_val+extra)
        if (rd.uniform(0,1)<EP.mutability):
            new_W1_y+=rd.uniform(UP.y_min,UP.y_max)-(0.5*abs(UP.y_max-UP.y_min))
            
        max_val = max(genelist[parent_1].W2_x,genelist[parent_2].W2_x)
        min_val = min(genelist[parent_1].W2_x,genelist[parent_2].W2_x)
        extra=(max_val-min_val)*(EP.merge_range)
        new_W2_x=rd.uniform(min_val-extra,max_val+extra)
        if (rd.uniform(0,1)<EP.mutability):
            new_W2_x+=rd.uniform(UP.x_min,UP.x_max)-(0.5*abs(UP.x_max-UP.x_min))
        
        max_val = max(genelist[parent_1].W2_y,genelist[parent_2].W2_y)
        min_val = min(genelist[parent_1].W2_y,genelist[parent_2].W2_y)
        extra=(max_val-min_val)*(EP.merge_range)
        new_W2_y=rd.uniform(min_val-extra,max_val+extra)
        if (rd.uniform(0,1)<EP.mutability):
            new_W2_y+=rd.uniform(UP.y_min,UP.y_max)-(0.5*abs(UP.y_max-UP.y_min))
            
        max_val = max(genelist[parent_1].SC,genelist[parent_2].SC)
        min_val = min(genelist[parent_1].SC,genelist[parent_2].SC)
        extra=(max_val-min_val)*(EP.merge_range)
        new_SC=rd.uniform(min_val-extra,max_val+extra)
        if (rd.uniform(0,1)<EP.mutability):
            new_SC+=rd.uniform(0,UP.SC_max)-(0.5*abs(UP.SC_max))
            
        # Set the fitness parameter to zero and generate the new generation gene            
        new_d=0
        new_genelist.append(Gene(new_M1_x,new_M1_y,new_M2_x,new_M2_y,new_W1_x,new_W1_y,new_W2_x,new_W2_y,new_SC,new_d))
        
    return new_genelist



def test_function(gen,UP):
    '''
    Just a test function to check the algorithm is working fine.
    '''
    dummy=100-abs(5-gen.M1_x)-abs(5-gen.M1_y)-abs(5-gen.M2_x)-abs(5-gen.M2_y)-abs(5-gen.W1_x)-abs(5-gen.W1_y)-abs(5-gen.W2_x)-abs(5-gen.W2_y)-abs(25-gen.SC)
    return [dummy,[1,2,3,4],[10,20,30,40],[1,2,3,4],[10,20,30,40],[1,2,3,4],[10,20,30,40],[1,2,3,4],[10,20,30,40],[1,2,3,4]]
        