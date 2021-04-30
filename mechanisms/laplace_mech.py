import numpy as np

"""
Laplce mechanism implemented using Lapclace distribution. The mechanism 
adds Laplace noise according to the parameters provided. 
:param x: original data to be applied the noise to 
:param epsilon: used to calibrate the noise according to the privacy budget
:param sensitivity: used to specify the sensitivity of a query in order to calibrate the noise
:param upper_limit: used to specify the upper limite of the ouput
"""


def laplaceMechanism(x, epsilon, sensitivity, upper_limit):
    not_in_range = True
    while (not_in_range):
        private_val = x + np.random.laplace(0, sensitivity/epsilon, 1)[0]
        if (private_val > upper_limit):
            private_val = upper_limit
            not_in_range = False
        if (private_val > 0):
            not_in_range = False
    return private_val
