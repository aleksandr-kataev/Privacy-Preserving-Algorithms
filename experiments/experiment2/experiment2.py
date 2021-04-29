import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os.path
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../mechanisms")))
from gaussian_mech import gaussianMechanism
from laplace_mech import laplaceMechanism


def experiment2(dataset_path, mech_type, epsilon, num_of_runs):
    dataset = pd.read_csv(dataset_path)
    normal_sensitivity = 1
    mean_age_sensitivity = (60 - 16) / len(dataset)
    delta = 1/1000
    wage_query = np.sum(dataset['wage'] < 10)
    age_query = np.sum(dataset['age'] > 30)
    mean_age_query = dataset['age'].mean()
    insured_query = np.sum(dataset['insured'] == True)
    histogram_query = [
        np.sum(dataset['problem'] == 'breathing'),
        np.sum(dataset['problem'] == 'dental'),
        np.sum(dataset['problem'] == 'mental'),
        np.sum(dataset['problem'] == 'heart')
    ]
    combined_query_join = dataset.query('age > 35 & wage > 10')
    combined_query = len(combined_query_join)

    wage_average = []
    age_average = []
    mean_age_average = []
    insured_average = []
    heart_average = []
    dental_average = []
    mental_average = []
    breathing_average = []
    combined_average = []

    if mech_type == "laplace":
        for x in range(num_of_runs):
            private_wage_query = laplaceMechanism(
                wage_query, epsilon, 1, len(dataset))
            wage_average.append(private_wage_query)
            private_age_query = laplaceMechanism(
                age_query, epsilon, 1, len(dataset))
            age_average.append(private_age_query)
            private_mean_age_query = laplaceMechanism(
                mean_age_query, epsilon, mean_age_sensitivity, len(dataset))
            mean_age_average.append(private_mean_age_query)
            private_insured = laplaceMechanism(
                insured_query, epsilon, 1, len(dataset))
            insured_average.append(private_insured)
            private_heart = laplaceMechanism(
                histogram_query[0], epsilon, 1, len(dataset))
            heart_average.append(private_heart)
            private_dental = laplaceMechanism(
                histogram_query[1], epsilon, 1, len(dataset))
            dental_average.append(private_dental)
            private_mental = laplaceMechanism(
                histogram_query[2], epsilon, 1, len(dataset))
            mental_average.append(private_mental)
            private_breathing = laplaceMechanism(
                histogram_query[3], epsilon, 1, len(dataset))
            breathing_average.append(private_breathing)
            private_combined = laplaceMechanism(
                combined_query, epsilon, 2, len(dataset))
            combined_average.append(private_combined)

    elif mech_type == 'gaussian':
        for x in range(num_of_runs):
            private_wage_query = gaussianMechanism(
                wage_query, epsilon, 1, delta, len(dataset))
            wage_average.append(private_wage_query)
            private_age_query = gaussianMechanism(
                age_query, epsilon, 1, delta, len(dataset))
            age_average.append(private_age_query)
            private_mean_age_query = gaussianMechanism(
                mean_age_query, epsilon, mean_age_sensitivity, delta, len(dataset))
            mean_age_average.append(private_mean_age_query)
            private_insured = gaussianMechanism(
                insured_query, epsilon, 1, delta, len(dataset))
            insured_average.append(private_insured)
            private_heart = gaussianMechanism(
                histogram_query[0], epsilon, 1, delta, len(dataset))
            heart_average.append(private_heart)
            private_dental = gaussianMechanism(
                histogram_query[1], epsilon, 1, delta, len(dataset))
            dental_average.append(private_dental)
            private_mental = gaussianMechanism(
                histogram_query[2], epsilon, 1, delta, len(dataset))
            mental_average.append(private_mental)
            private_breathing = gaussianMechanism(
                histogram_query[3], epsilon, 1, delta, len(dataset))
            breathing_average.append(private_breathing)
            private_combined = gaussianMechanism(
                combined_query, epsilon, np.sqrt(2), delta, len(dataset))
            combined_average.append(private_combined)

    else:
        raise ValueError("incorrect argument for mechanims type")

    print("Original wage query ", wage_query)
    print("Wage average ", round(np.mean(wage_average), 4))
    print("Wage percentage ", round(
        ((np.mean(wage_average) - wage_query) / wage_query) * 100, 4))
    print("-------------------")
    print("Original age query ", age_query)
    print("Age average ", round(np.mean(age_average), 4))
    print("Age percentage ", round(
        ((np.mean(age_average) - age_query) / age_query) * 100, 4))
    print("-------------------")
    print("Original mean age query ", mean_age_query)
    print("Mean age average ", round(np.mean(mean_age_average), 4))
    print("Mean age percentage ", round(
        ((np.mean(mean_age_average) - mean_age_query) / mean_age_query) * 100, 4))
    print("-------------------")
    print("Original insured query ", insured_query)
    print("Insured average ", round(np.mean(insured_average), 4))
    print("Insured percentage ", round(
        ((np.mean(insured_average) - insured_query) / insured_query) * 100, 4))
    print("-------------------")
    print("Original heart query ", histogram_query[0])
    print("Heart average ", round(np.mean(heart_average), 4))
    print("Heart average percentage ", round(
        ((np.mean(heart_average) - histogram_query[0]) / histogram_query[0]) * 100, 4))
    print("-------------------")
    print("Original dental query ", histogram_query[1])
    print("Dental average ", round(np.mean(dental_average), 4))
    print("Dental average percentage ", round(
        ((np.mean(dental_average) - histogram_query[1]) / histogram_query[1]) * 100, 4))
    print("-------------------")
    print("Original mental query ", histogram_query[2])
    print("Mental average ", round(np.mean(mental_average), 4))
    print("Mental average percentage ", round(
        ((np.mean(mental_average) - histogram_query[2]) / histogram_query[2]) * 100, 4))
    print("-------------------")
    print("Original breathing query ", histogram_query[3])
    print("Breathing average ", round(np.mean(breathing_average), 4))
    print("Breathing average percentage ", round(
        ((np.mean(breathing_average) - histogram_query[3]) / histogram_query[3]) * 100, 4))
    print("-------------------")
    print("Original combined query ", combined_query)
    print("Combined query average ", round(np.mean(combined_average), 4))
    print("Combined query average percentage ", round(
        ((np.mean(combined_average) - combined_query) / combined_query) * 100, 4))
