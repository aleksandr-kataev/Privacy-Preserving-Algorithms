import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os.path
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../mechanisms")))
from gaussian_mech import gaussianMechanism
from laplace_mech import laplaceMechanism
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from metrics import rmse_var, rmse_arr, mape_var, mape_arr


EPSILONS = np.logspace(0, 3, 50)
DATASET = pd.read_csv('../../datasets/large_dataset.csv')
WAGE_QUERY = np.sum(DATASET['wage'] < 10)
COMBINED_QUERY_JOIN = DATASET.query('age > 35 & wage > 10')
COMBINED_QUERY = len(COMBINED_QUERY_JOIN)
HISTOGRAM_QUERY = [
    np.sum(DATASET['problem'] == 'breathing'),
    np.sum(DATASET['problem'] == 'dental'),
    np.sum(DATASET['problem'] == 'mental'),
    np.sum(DATASET['problem'] == 'heart')
]
NUM_OF_RUNS = 5000
DELTA_VALUES = [1/500, 1/1000, 1/10000, 1/100000]
COLORS = ['r', 'b', 'g', 'c']


def test3(mech_type, query_type):
    if mech_type == 'laplace' and query_type == 'wage':
        laplace_wage()
    elif mech_type == 'laplace' and query_type == 'combined':
        laplace_combined()
    elif mech_type == 'laplace' and query_type == 'histogram':
        laplace_histogram()
    elif mech_type == 'gaussian' and query_type == 'wage':
        gaussian_wage()
    elif mech_type == 'gaussian' and query_type == 'combined':
        gaussian_combined()
    elif mech_type == 'gaussian' and query_type == 'histogram':
        gaussian_histogram()
    else:
        raise ValueError("incorrect argument supplied")


def display_laplace(rmse, mape, label):
    plt.semilogx(EPSILONS, rmse)
    plt.xlabel('Epsilon')
    plt.ylabel('Error')
    plt.title("RMSE " + label + " Laplace")
    plt.show()

    plt.semilogx(EPSILONS, mape)
    plt.xlabel('Epsilon')
    plt.ylabel('Error')
    plt.title("MAPE " + label + " Laplace")
    plt.show()


def display_gaussian(error_arr, label):
    for idx, error in enumerate(error_arr):
        plt.semilogx(EPSILONS, error[0], COLORS[idx])

    plt.xlabel('Epsilon')
    plt.ylabel('Error')
    plt.title("RMSE " + label + " Gaussian")
    plt.show()

    for idx, error in enumerate(error_arr):
        plt.semilogx(EPSILONS, error[1], COLORS[idx])

    plt.xlabel('Epsilon')
    plt.ylabel('Error')
    plt.title("MAPE " + label + " Gaussian")
    plt.show()


def laplace_wage():
    laplace_rmse_wage = []
    laplace_mape_wage = []
    for epsilon in EPSILONS:
        average_rmse = []
        average_mape = []
        for x in range(NUM_OF_RUNS):
            private_wage_query = laplaceMechanism(WAGE_QUERY, epsilon, 1, 1000)
            average_rmse.append(rmse_var(WAGE_QUERY, private_wage_query))
            average_mape.append(mape_var(WAGE_QUERY, private_wage_query))
        laplace_rmse_wage.append(np.mean(average_rmse))
        laplace_mape_wage.append(np.mean(average_mape))

    display_laplace(laplace_rmse_wage, laplace_mape_wage, "Wage")


def laplace_combined():
    laplace_rmse_combined = []
    laplace_mape_combined = []
    for epsilon in EPSILONS:
        average_rmse = []
        average_mape = []
        for x in range(NUM_OF_RUNS):
            private_combined_query = laplaceMechanism(
                COMBINED_QUERY, epsilon, 2, 1000)
            average_rmse.append(
                rmse_var(COMBINED_QUERY, private_combined_query))
            average_mape.append(
                mape_var(COMBINED_QUERY, private_combined_query))
        laplace_rmse_combined.append(np.mean(average_rmse))
        laplace_mape_combined.append(np.mean(average_mape))

    display_laplace(laplace_rmse_combined, laplace_mape_combined, "Combined")


def laplace_histogram():
    laplace_rmse_histogram = []
    laplace_mape_histogram = []
    for epsilon in EPSILONS:
        average_rmse = []
        average_mape = []
        for x in range(NUM_OF_RUNS):
            private_histogram_query = []
            for value in HISTOGRAM_QUERY:
                private_histogram_query.append(
                    laplaceMechanism(value, epsilon, 1, 1000))
            average_rmse.append(rmse_arr(
                HISTOGRAM_QUERY, private_histogram_query))
            average_mape.append(mape_arr(
                HISTOGRAM_QUERY, private_histogram_query))
        laplace_rmse_histogram.append(np.mean(average_rmse))
        laplace_mape_histogram.append(np.mean(average_mape))

    display_laplace(laplace_rmse_histogram,
                    laplace_mape_histogram, "Histogram")


def gaussian_wage():
    gaussian_wage_error = []
    for delta_value in DELTA_VALUES:
        gaussian_rmse = []
        gaussian_mape = []
        for epsilon in EPSILONS:
            average_rmse = []
            average_mape = []
            for x in range(NUM_OF_RUNS):
                private_wage_query = gaussianMechanism(
                    WAGE_QUERY, epsilon, 1, delta_value, 1000)
                average_rmse.append(rmse_var(WAGE_QUERY, private_wage_query))
                average_mape.append(mape_var(WAGE_QUERY, private_wage_query))
            gaussian_rmse.append(np.mean(average_rmse))
            gaussian_mape.append(np.mean(average_mape))
        gaussian_wage_error.append([gaussian_rmse, gaussian_mape])

    display_gaussian(gaussian_wage_error, "Wage")


def gaussian_combined():
    gaussian__combined_error = []
    for delta_value in DELTA_VALUES:
        gaussian_rmse = []
        gaussian_mape = []
        for epsilon in EPSILONS:
            average_rmse = []
            average_mape = []
            for x in range(NUM_OF_RUNS):
                private_combined_query = gaussianMechanism(
                    COMBINED_QUERY, epsilon, np.sqrt(2), delta_value, 1000)
                average_rmse.append(
                    rmse_var(COMBINED_QUERY, private_combined_query))
                average_mape.append(
                    mape_var(COMBINED_QUERY, private_combined_query))
            gaussian_rmse.append(np.mean(average_rmse))
            gaussian_mape.append(np.mean(average_mape))
        gaussian__combined_error.append([gaussian_rmse, gaussian_mape])

    display_gaussian(gaussian__combined_error, "Combined")


def gaussian_histogram():
    gaussian_histogram_error = []
    for delta_value in DELTA_VALUES:
        gaussian_rmse = []
        gaussian_mape = []
        for epsilon in EPSILONS:
            average_rmse = []
            average_mape = []
            for x in range(NUM_OF_RUNS):
                private_histogram_query = []
                for value in HISTOGRAM_QUERY:
                    private_histogram_query.append(gaussianMechanism(
                        value, epsilon, 1, delta_value, 1000))

                average_rmse.append(
                    rmse_arr(HISTOGRAM_QUERY, private_histogram_query))
                average_mape.append(
                    mape_arr(HISTOGRAM_QUERY, private_histogram_query))

            gaussian_rmse.append(np.mean(average_rmse))
            gaussian_mape.append(np.mean(average_mape))
        gaussian_histogram_error.append([gaussian_rmse, gaussian_mape])

    display_gaussian(gaussian_histogram_error, "Histogram")
