#!/usr/bin/env python

import numpy as np

# Function to calculate y-coordinates of the circle:
def coordinates(x,R):
    """
    This function calculates the y values of a circle with radius R.\
    The size of the y array will be double to that of the input x array.
    Input: Array of x-axis points
           Radius of circle 
    Output: Array of y values
    """
    
    # Numpy is imported from inside function in case it has not been previously imported
    import numpy as np
    
    y = np.sqrt(R**2-x**2)
    y = np.append(y,-np.sqrt(R**2-x**2))
    
    return y

# Function to calculate diameter and surface area of sphere:
def sphere_properties(R):
    """
    This function uses the radius of a sphere to calculate its diameter and surface area.
    Input: Radius [float]
    Output: [Diameter, Surface Area] [List]
    """
    
    # Numpy is imported from inside function in case it has not been previously imported
    import numpy as np
    
    # Diameter of sphere
    D = 2*R
    # Surface area of sphere
    SA = 4*np.pi*R**2
    
    return [D,SA]

# Create array of x coordinates:

x = -10. + np.arange(0, 20.1, 0.1) 

# Ask for input R:


# Call the external functions:


# Print informative statements:
