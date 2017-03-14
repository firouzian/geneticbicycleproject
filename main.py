import Genetics
import matplotlib.pyplot as plt
#from Genetics import Create_Genelist
from gene import Gene
from user_parameters import User_Parameters
from evolution_parameters import Evolution_Parameters
import numpy as np
import scipy as sp
import random as rd

# -------------------Set User Parameters Values--------------------------- 
# (we can ask this by command line, but first is easier to just hardcode it)

# Box in wich the bicycle can appear in the first generation of genes
x_min = 0
y_min = 0
x_max = 10
y_max = 10
# Max value of the Spring Constant for the first generation of genes 
SC_max = 50
# Parameters for the Ground in wich the bicycle will move
amplitude = 1
slope = -0.2

UP=User_Parameters(x_min, y_min, x_max, y_max, SC_max,amplitude,slope)

# -----------------Set the Evolution Parameters----------------------------

# Total number of bicycles (genes) in each generation
num_genes = 300
# Number of generation we want to evolve
num_generations = 40
# Range in wich new generation can ecxeed the parents parameters
merge_range=0.05
# Chance of mutation
mutability=0.005
 
EP=Evolution_Parameters(merge_range,mutability,num_genes,num_generations)


# ----------------Creation of our first generation -------------------------

Genes=Genetics.Create_Genelist(EP,UP)


# -------------------------- TEST TEST TEST --------------------------------


# Testing the algorithm, all M1_x parameters should aproach number 5
print('Test Function: Max in 5 for all positions and 25 for the Spring Constant')
print()

rand_bike=rd.randint(0,(EP.num_genes-1))

print ('First Generation:')
print (Genes[rand_bike].M1_x)
print (Genes[rand_bike].M1_y)
print (Genes[rand_bike].M2_x)
print (Genes[rand_bike].M2_y)
print (Genes[rand_bike].W1_x)
print (Genes[rand_bike].W1_y)
print (Genes[rand_bike].W2_x)
print (Genes[rand_bike].W2_y)
print (Genes[rand_bike].SC)
print()

mean_d=[]
max_d=[]
for i in range(EP.num_generations):
    d_list=np.zeros(len(Genes))
    i = 0
    for gen in Genes:
        # Testing the fitness of each bicycle (gen)
        gen.d=Genetics.test_function(gen,UP)
        d_list[i]=gen.d
        i+=1
    mean_d.append(np.mean(d_list))
    max_d.append(np.max(d_list))    
    # Evolve the whole population (list of genes) to create a new generation (list) of bicycles (genes)
    Genes=Genetics.Evolve_Genes(Genes,EP,UP)
    

print ('Last Generation:')    
print (Genes[rand_bike].M1_x)
print (Genes[rand_bike].M1_y)
print (Genes[rand_bike].M2_x)
print (Genes[rand_bike].M2_y)
print (Genes[rand_bike].W1_x)
print (Genes[rand_bike].W1_y)
print (Genes[rand_bike].W2_x)
print (Genes[rand_bike].W2_y)
print (Genes[rand_bike].SC)
print()

plt.plot(range(len(max_d)),max_d,range(len(max_d)),mean_d)