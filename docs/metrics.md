# Metrics

The following metrics are used a measure of error in the experiments
</br>
</br>
## Root mean squared error

Root-mean-square error (RMSE) is a measure of the differences between values predicted by a model or an estimator and the values observed. It can be defined as:

![RMSE](https://latex.codecogs.com/svg.image?RMSE&space;=&space;\sqrt{\frac{\sum_{i=1}^{n}&space;(x_{i}&space;-&space;y_{i})^2}{n}})


In my case, I compare the original data with the anonymised data to determine the difference.
</br>
</br>
## Mean absolute percentage error

Mean absolute percentage error is a measure of prediction accuracy. It expresses the accuracy as a ratio defined by the formula:

![MAPE](https://latex.codecogs.com/svg.image?MAPE&space;=&space;\frac{1}{n}&space;\sum_{i=1}^{n}&space;\left|\frac{x_{i}&space;-&space;y_{i}}{x_{i}}&space;\right|&space;*&space;100)

The metrics file has 4 functions:
1. mape_var: used to calculate MAPE between two variables which esentially is a percentage difference
1. rmse_var: used to calculate the RMSE between two variables
1. mape_arr: Used to calculate the MAPE between the original and anonymised arrays of data.
1. rmse_arr: Used to calculate the RMSE between the original and anonymised arrays of data.

Some queries such as "how many people are over 35" only require the difference between two numbers while histogram queries require the difference between two arrays. This is the reason two variations of RMSE and MAPE were implemented. 

The rmse_arr function is implemented using function provided by sklearn package.