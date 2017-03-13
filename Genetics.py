#!/usr/bin/python

# Genetic part of Genetic Bicycle project
import numpy as np
import scipy as sp
import random as rd
from gene import Gene
from user_parameters import User_Parameters

# Defines a function that creates a list of n random genes
#   Those genes are restrected some ranges defined by the user
def Create_Genelist(num,UP):
    GL=[]
    for i in range(num):
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
    
