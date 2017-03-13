import Genetics
#from Genetics import Create_Genelist
from gene import Gene
from user_parameters import User_Parameters
from evolution_parameters import Evolution_Parameters
import numpy as np
import scipy as sp
import random as rd

# Set user Parameters Values (we can ask this by command line, but first is easier to just hardcode it)
x_min = 0
y_min = 0
x_max = 10
y_max = 10
SC_max = 50
UP=User_Parameters(x_min, y_min, x_max, y_max, SC_max)

# Set the Evolve Parameters
merge_range=0.01 # Range in wich new generation can ecxeed the parents parameters
mutability=0.001 # Chance of mutation
EP=Evolution_Parameters(merge_range,mutability)


# TEST

# Testing the algorithm, all M1_x parameters should aproach number 5
print('Test Function: d=10-abs(M1_x-5)')
print()

Genes=Genetics.Create_Genelist(100,UP)
print ('First Generation:')
print (Genes[0].M1_x)
print (Genes[1].M1_x)
print (Genes[2].M1_x)
print (Genes[3].M1_x)
print()

for i in range(1000):
    for gen in Genes:
        gen.d=Genetics.test_function(gen,UP)
    Genes=Genetics.Evolve_Genes(Genes,EP,UP)
print ('Last Generation:')    
print (Genes[0].M1_x)
print (Genes[1].M1_x)
print (Genes[2].M1_x)
print (Genes[3].M1_x)