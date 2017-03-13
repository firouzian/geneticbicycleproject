#!/usr/bin/python

# Is a class that contain all the information of a bicycle gene (parameters that can evolve)

class Gene(object):
    """Station class"""
    def __init__(self, M1_x, M1_y, M2_x, M2_y, W1_x, W1_y, W2_x, W2_y, SC, d=0):
        self.M1_x = M1_x
        self.M1_y = M1_y  
        self.M2_x = M2_x  
        self.M2_y = M2_y
        self.W1_x = W1_x
        self.W1_y = W1_y
        self.W2_x = W2_x
        self.W2_y = W2_y
        self.SC = SC   
        self.d = d  
         
         
# This function take as an imput the User Settings (another class of the program)
# that contain the information of the range in wich genes are considered Good Genes 

    def is_good(self,UP):

        """Gene check Function"""

        x_check = (UP.x_min < self.M1_x < UP.x_max ) and (UP.x_min < self.M2_x < UP.x_max ) and (UP.x_min < self.W1_x < UP.x_max )and (UP.x_min < self.W2_x < UP.x_max) 
        y_check = (UP.y_min < self.M1_y < UP.y_max ) and (UP.y_min < self.M2_y < UP.y_max ) and (UP.y_min < self.W1_y < UP.y_max )and (UP.y_min < self.W2_y < UP.y_max) 
        SC_check = self.SC < UP.SC_max        
        if (x_check and y_check and SC_check):
            return 1
        else:
            return 0
