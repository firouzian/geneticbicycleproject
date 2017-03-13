from Genetics import Create_Genelist
from gene import Gene
from user_parameters import User_Parameters
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

Genes=Create_Genelist(1,UP)