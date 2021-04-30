# Satisfying ε-differntial privacy

This test involves observing the results of the algorithms implemented to see whether they satisfy the definition of ε-differntial privacy.

Two adjecent datasets of size 200 and 199 are used for test the mechnisms using the queries with different sensitivities. 

## Laplace configuration
</br>

- ε = 1
- num_of_runs = 20

Queries used:
1. How many people earn less than £10? Sensitivity = 1
1. How many people are over he age of 25 and earn more than £10? Sensitivity = 2

## Gaussian configuration
</br>

- ε = 1
- δ = 1/200
- num_of_runs = 20

Queries used:
1. How many people earn less than £10? Sensitivity = 1
1. How many people are over he age of 25 and earn more than £10? Sensitivity = √2

The test is run 20 times for each mechnism using each query. The mechnisms are used on both datasets and the highest difference between the output of the adjacent datasets are selected to compare. Using the defintion of the differential privacy an inequality is constructed indicating whether the output satisfies the definition. The results can be observed in test1 jupyter notebook.