import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os.path
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../mechanisms")))
from gaussian_mech import gaussianMechanism
from laplace_mech import laplaceMechanism

"""
This test involves looking at how the mechanisms implemeted satisfy the definition of ε-differntial privacy. 
:param mech_type: type of mechnism to test (laplace or gaussian)
:param query_type: type of query to test (wage or combined)
:param epsilon: used to calibrate the noise according to the privacy budget
:param sensitivity: used to specify the sensitivity of a query in order to calibrate the noise
:param num_of_runs: used to specify the number of run for the test
:returns: a graph showing how results of queries from adjacent databases differ after applying mechanisms
"""


def test1(mech_type, query_type, epsilon, sensitivity, num_of_runs):
    dataset = pd.read_csv("../../datasets/small_dataset.csv")
    delta = 1/200
    adj_dataset = dataset.iloc[1:]
    upper_limit = len(dataset)
    adj_upper_limit = len(adj_dataset)

    if query_type == "wage":
        query = np.sum(dataset['wage'] < 10)
        adj_query = np.sum(adj_dataset['wage'] < 10)
    elif query_type == "combined":
        query_join = dataset.query('age > 35 & wage > 10')
        query = len(query_join)
        adj_query_join = adj_dataset.query('age > 35 & wage > 10')
        adj_query = len(adj_query_join)
    else:
        raise ValueError("incorrect argument for query type")

    normal_average = []
    adj_average = []

    if mech_type == "laplace":
        for x in range(num_of_runs):
            private_query = laplaceMechanism(
                query, epsilon, sensitivity, upper_limit)
            private_adj_query = laplaceMechanism(
                adj_query, epsilon, sensitivity, adj_upper_limit)
            normal_average.append(private_query)
            adj_average.append(private_adj_query)
    elif mech_type == "gaussian":
        for x in range(num_of_runs):
            private_query = gaussianMechanism(
                query, epsilon, sensitivity, delta, upper_limit)
            private_adj_query = gaussianMechanism(
                adj_query, epsilon, sensitivity, delta, adj_upper_limit)
            normal_average.append(private_query)
            adj_average.append(private_adj_query)
    else:
        raise ValueError("incorrect argument for mechanims type")

    runs = list(range(1, num_of_runs + 1))
    plt.plot(runs, normal_average, 'r')
    plt.plot(runs, adj_average, 'b')
    plt.xlabel('Runs')
    plt.ylabel('Query result')
    plt.xticks(runs)
    plt.show()

    difference_of_averages = []
    
    for idx, value in enumerate(normal_average):
        difference_of_averages.append(abs(value - adj_average[idx]))
    
    highest_difference = max(difference_of_averages)
    highest_difference_idx = difference_of_averages.index(highest_difference)
    normal_value = normal_average[highest_difference_idx]
    adj_value = adj_average[highest_difference_idx]
    run_index = highest_difference_idx

    if mech_type == "gaussian":
        upper_result_limit = np.exp(epsilon) * min(normal_value, adj_value) + delta
    elif mech_type == 'laplace':
        upper_result_limit = np.exp(epsilon) * min(normal_value, adj_value)
    print("Run number: ", run_index + 1)
    print("200 individuals value: ", normal_value)
    print("199 individuals value: ", adj_value)
    print("Upper limit: ", upper_result_limit)
    
    if min(normal_value, adj_value) <= upper_result_limit:
        print("Satisfies the definition of differential privacy")
    else:
        print("Does not satisfy the definition of differential privacy")
