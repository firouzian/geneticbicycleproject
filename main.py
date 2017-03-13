import Genetics
#from Genetics import Create_Genelist
from gene import Gene
from user_parameters import User_Parameters
from evolution_parameters import Evolution_Parameters
import numpy as np
import scipy as sp
import random as rd

# Set user Parameters Values (we can ask this by command line, but first is easier to just hardcode it)

# Box in wich the bicycle can appear in the first generation of genes
x_min = 0
y_min = 0
x_max = 10
y_max = 10
# Max value of the Spring Constant for the first generation of genes 
SC_max = 50

UP=User_Parameters(x_min, y_min, x_max, y_max, SC_max)

# Set the Evolve Parameters

# Total number of bicycles (genes) in each generation
num_genes = 200
# Number of generation we want to evolve
num_generations = 1000
# Range in wich new generation can ecxeed the parents parameters
merge_range=0.02
# Chance of mutation
mutability=0.001
 
EP=Evolution_Parameters(merge_range,mutability,num_genes,num_generations)


# TEST

# Testing the algorithm, all M1_x parameters should aproach number 5
print('Test Function: Max in 5 for all positions and 25 for the Spring Constant')
print()

Genes=Genetics.Create_Genelist(EP,UP)
print ('First Generation:')
print (Genes[0].M1_x)
print (Genes[0].M1_y)
print (Genes[0].M2_x)
print (Genes[0].M2_y)
print (Genes[0].W1_x)
print (Genes[0].W1_y)
print (Genes[0].W2_x)
print (Genes[0].W2_y)
print (Genes[0].SC)
print()

for i in range(EP.num_generations):
    for gen in Genes:
        gen.d=Genetics.test_function(gen,UP)
    Genes=Genetics.Evolve_Genes(Genes,EP,UP)
print ('Last Generation:')    
print (Genes[0].M1_x)
print (Genes[0].M1_y)
print (Genes[0].M2_x)
print (Genes[0].M2_y)
print (Genes[0].W1_x)
print (Genes[0].W1_y)
print (Genes[0].W2_x)
print (Genes[0].W2_y)
print (Genes[0].SC)
print()