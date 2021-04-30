# Observing the behaviour of the mechanisms

For this test, I have tested and studied the behaivour of the mechnisms using all the queries avaliable with different sensitivities. A dataset of 200 and 1000 individuals is used for this test. 

# Configuration

- ε = 1
- δ = 1/1000 (used for Gaussian mechanism)
<br/>

Queries used:


| Query     | Laplace sensitivity | Gaussian sensitivity     |
| :---        |    :----:   |          :----: |
| How many people earn more less £10?      | 1       | 1   |
| How many people are over 30 years of age?   | 1       | 1      |
| Mean number of age in the database?   | (60 - 16) / len(dataset)       | (60 - 16) / len(dataset)      |
| How many people are insured? | 1        | 1      |
| How many people are over 35 and earn more than £10?   | 2       |   √2    |
| Histogram queries   | 1        | 1      |

<br/>
<sub>Sensitivity for the mean query is calculated as (upper_age_limit - lower_age_limit ) / dataset_length.
Histogram queries invloves retreiving the number of individuals for each health problem from the dataset.</sub>
</br>
<br/>
The test was run 100 times for each(). The average number of 100 runs has been recorded as well as the percentage change. The results can be observed in test2 jupyter notebook.