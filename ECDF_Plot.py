import numpy as np
import matplotlib.pyplot as plt

def ecdf(data, xlab, ylab):
    
    """
    Args - data: array
           xlab: Label for x axis
           ylab: Label for y axis
    Function: Plots ECDF
    """
    
    # Number of data points
    nums = len(data)
    # x axis data
    x = np.sort(data)
    # y axis data
    y = np.arange(1, nums + 1) / nums
    
    # Plot ecdf
    plt.plot(x, y, marker='.', linestyle='none')
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.title(xlab + " VS " + ylab)
    plt.show()
