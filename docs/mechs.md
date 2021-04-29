# Implementation of differentially private mechanisms

Differentially private mechnisms work by adding a scalled noise to the dataset or a result of query. 

<img src="https://miro.medium.com/max/1172/1*6_roTu-UE6kUBd7rU7Uh7g.png" alt="drawing" width="500"/>

The simplest example of a differentially private mechanism is a randomised response mechanism.

## Randomised response

Suppose a data analyst would like to carry out a survey to know how many people smoke. The mechanism works by adding noise on the answers recorded and works in the following way:
1. Flip a coin
1. If it lands tails, respond truthfully
1. If it lands heads, flip a second coin and record “yes” if it lands heads and “no” if it lands tails

As a result a noise is introduces to the data. However, the data analyst can still calculate the approximate number of people who smoke as the probabilities or a coin landing heads, or tails are known. At the same time, this offers plausible deniability as a person answering ‘yes’ might not necessarily smoke. In this case the epsilon is 3.

For this project I have mainly focused on Laplace and Gaussian mechanisms.
<br/>
<br/>
## Laplace mechanism

Laplce mechnism uses a pure notion of differential privacy with δ = 0. For this mechanism, Laplace distribution is used to generate noise which is defined as: 


![laplce-definition](https://latex.codecogs.com/svg.image?f(x|\mu,&space;b)&space;=&space;\tfrac{1}{2b}*e^{\frac{\left|x&space;-&space;\mu&space;\right|}{b}})


The image shows an example of laplace distributions with difffernt scales


<img src="https://upload.wikimedia.org/wikipedia/commons/0/0a/Laplace_pdf_mod.svg" alt="drawing" width="500"/>


In my case the µ is 0 as the position at which the distribution peaks in 0. The diagram shows examples of Laplace distributions with different μ and b. The scale of the distribution defined as b is calculated as 


![sensitivity](https://latex.codecogs.com/svg.image?\frac{\Delta&space;F}{\varepsilon&space;})

<sub>where delta F is the sensitinity of the query and ε is the epsilon parameter</sub>
</br>
</br>
The private result is computed as:


![laplace-mechnism](https://latex.codecogs.com/svg.image?F(x)&space;=&space;f(x)&space;&plus;&space;Lap(\frac{\Delta&space;F}{\varepsilon&space;}))
<br/>
<br/>
## Gaussian mecchanism


Gaussian mechanism works in a similar way however, gaussian distribution is used. This mechanism does not satisfy pure ε-differential privacy, but does satisfy (ε, δ)-differential privacy. The parameter δ is introduced which is described in the definition of differntial privacy. In addition Gaussian mechanism uses l2 norm sensitivity rather than l1 which is used by Laplce mechanism. This means that the definition of the sensitivity described in the introduction documentation changes to:
<br/>
<br/>
![l2 sensitivity](https://latex.codecogs.com/svg.image?\Delta&space;F&space;=&space;max_{x1,x2}\left|\left|F(D1)&space;-&space;F(D2)&space;\right|\right|_{2})
<br/>
<br/>

This proves to perform better for a certain types of qureies as in some cases l1 sensitivity is higher than l2.


The diagram shows examples of Gaussian distributions with different μ and σ^2. The sampling from the Gaussian distribution with centre 0 and variance σ^2 is defined by the following:


![laplce-definition](https://latex.codecogs.com/svg.image?\sigma^2&space;=&space;\frac{2s^2log(\frac{1.25}{\delta&space;})}{\varepsilon^2}&space;)

<sup>s refers to the sensitivity of a query and δ refres to the delta value</sup>

The image shows an example of laplace distributions with difffernt scales.

<img src="https://upload.wikimedia.org/wikipedia/commons/7/74/Normal_Distribution_PDF.svg" alt="drawing" width="500"/>


Both mechnism accept x, epsilon, and upper_limit as their parameters while Gaussian mechanism also accepts delta.

1. x: original data to be applied the noise to 
1. epsilon: used to calibrate the noise according to the privacy budget
1. sensitivity: used to specify the sensitivity of a query in order to calibrate the noise
1. upper_limit: used to specify the upper limite of the ouput
1. delta: used to specify the δ for the relaxed definition of differntial privacy

Mechanisms draw a random sample from the Gaussian and Laplace distributions scaled based on the epsilon and the sensitivity of the query. It then added to the original data. If the result is higher than the upper limit supplied the mechanisms return the upper limit supplied. However, if the result is less than 0, the algorithm draws another sample and adds to the original data until the condition is satisfied being the output should be more or equal to 0.

