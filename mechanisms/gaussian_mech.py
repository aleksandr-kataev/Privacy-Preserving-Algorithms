import numpy as np

"""
Gaussian mechanism implemented using Gaussian distribution. The mechanism 
adds Gaussian noise according to the parameters provided. 
:param x: original data to be applied the noise to 
:param epsilon: used to calibrate the noise according to the privacy budget
:param sensitivity: used to specify the sensitivity of a query in order to calibrate the noise
:param delta: used to specify the δ for the relaxed definition of differntial privacy
:param upper_limit: used to specify the upper limite of the ouput
"""

def gaussianMechanism(x, epsilon, sensitivity, delta, upper_limit):
    sigma = np.sqrt(2 * np.log(1.25 / delta)) * sensitivity / epsilon
    not_in_range = True
    while (not_in_range):
        private_val = x + np.random.normal(0, sigma, 1)[0]
        if (private_val > upper_limit):
            private_val = upper_limit
            not_in_range = False
        if (private_val >= 0):
            not_in_range = False
    return private_val