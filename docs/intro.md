# Introduction

## Differential privacy

This project mainly focuses on the differentially private mechanisms and experimenting with their behaviour.

### Definition

Differential privacy is a system for publicly sharing information about a dataset while withholding information about individuals in the dataset. The primary proposition of DP involves making sure a data subject is not affected (e.g. not harmed) by their entry or participation in a database, while maximizing utility/data accuracy for the queries.

It involves a conecpt of ε-differntial privacy which refers to a mathematical definition associated with the privacy loss of a data release from a statistical database. An algorithm A is ε-differentially private if the following hold true for any two neighbouring datasets D1 and D2 for all events S:
<br/>
<br/>
![pure differential privacy](https://latex.codecogs.com/svg.image?Pr[A(D1)\in&space;S&space;]&space;\leq&space;e^{\varepsilon&space;}&space;*&space;Pr[A(D2)\in&space;S&space;])
<br/>
<sup>For D1 and D2 differing in one element</sup>
</br>

While the definition above is a pure definition of differential privacy , another definition hold true defined as:
</br>

![approximate differential privacy](https://latex.codecogs.com/svg.image?Pr[A(D1)\in&space;S&space;]&space;\leq&space;e^{\varepsilon&space;}&space;*&space;Pr[A(D2)\in&space;S&space;]&space;&plus;&space;\delta&space;)
<br/>
<sup>For D1 and D2 differing in one element</sup>
</br>

This definition is a relaxation to the pure defintion as a variable δ is introduced and is denoted as (ε, δ)-differential privacy. δ is the probability of the data being accidentally leaked meaning that for all adjacent x, y, the absolute value of the privacy loss will be bounded by ε with probability at least 1−δ.

### Sensitivity

Sensitivity is a term used to measure how much one person can affect the output of a database and is defined as:
</br>
</br>
![l1 sensitivity](https://latex.codecogs.com/svg.image?\Delta&space;F&space;=&space;max_{x1,x2}\left|\left|F(D1)&space;-&space;F(D2)&space;\right|\right|_{1})

<sub>Where D1 and D2 differ at most in one element</sub>
</br>
</br>

Query such as "How many people earn more than £10?" have a sensitivity of 1 as one individual can change the count of query exactly by 1.

Sensitivity together with epsilon are used to scale the noise to be applied on the data. Generally speaking, the higher the sensitivity the more noise added, while the higher the epsilone the less noise is added. 
