import numpy as np

def Create_Ground(UP):
    '''
    Create a fixed list of points.
    
    The line joining those points is the ground of our problem
    '''
    amp = UP.amplitude
    slope = UP.slope
    x_minim = -2
    x_maxim = 20    
    GR = []
    x = np.arange(x_minim, x_maxim, 0.1)
    y = slope*x + amp*(np.sin(x*4*(np.pi)/float(x_maxim)))-2
    
    for i in range(len(x)):
        GR.append((x[i],y[i]))
        
    return GR