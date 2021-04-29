import numpy as np
from sklearn.metrics import mean_squared_error

"""
Metrics used to calculate the error for the experiments. 
"""

"""
Mean abosulte percetnage error for two variables
Used to calculate the percentage differnece between original and anonymised data.
:param original: original value
:param original: anonymised value
:return percentage differnce between original value and anonymised value
"""


def mape_var(original, anonymised):
    return np.abs((original - anonymised) / original) * 100


"""
Root mean squared error for two variables
Used to calculate the root mean squared error between two variables
:param original: original value
:param original: anonymised value
:return root mean squared error of original value and anonymised value
"""


def rmse_var(original, anonymised):
    return np.sqrt((anonymised - original)**2)


"""
Mean absolute percentage error for two arrays
Used to calculate the MAPE between the original and anonymised arrays of data.
:param original: an array of original values 
:param anonymised: an array of anonymised values 
:return: MAPE of original and anonymised values 
"""


def mape_arr(original, anonymised):
    original_np_arr, anonymised_np_arr = np.array(
        original), np.array(anonymised)
    return np.mean(np.abs((original_np_arr - anonymised_np_arr) / original_np_arr)) * 100


"""
Root mean squared error for two arrays
Used to calculate the RMSE between the original and anonymised arrays of data.
:param original: original value
:param original: anonymised value
:return root mean squared error of original value and anonymised value
"""


def rmse_arr(original, anonymised):
    return mean_squared_error(original, anonymised, squared=False)
