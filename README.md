# Privacy preserving algorithms in the release of healthcare data

## Abstract

Privacy plays an essential role when it comes to managing healthcare information. People classify
healthcare data as one of the most sensitive types of data and would not want it to be shared or
leaked. On the other hand, healthcare data can be used in fields such as patient care, medical
imaging, and research. With the data being so sensitive yet so useful, robust techniques must be put
in place to preserve privacy and utilise the information for the benefit of the public.

My project focuses on the comparison of different privacy-preserving algorithms that could be used
for a healthcare database or a query. Specifically, I focus on the differentially private algorithms and
compare the results of a query on a dataset that has had a differentially private mechanism applied
to it. The comparison involves Laplace and Gaussian mechanisms. With the use of a graph, I can
show how different parameters affect the behaviour of the mechanisms. I also look at how artificial
intelligence combined with differential privacy could be used in private data release by exploring the
PATE framework.

## Table of content

1. [Introduction](./docs/intro.md)
1. [Implementation](./docs/mechs.md)
1. Testing
	1. [Metrics](./docs/metrics.md)
	1. [Prooving ε-differntial privacy](./docs/test1.md)
	1. [Behavior of mechanisms for different queries](./docs/test2.md)
	1. [Utility-privacy trade-off](./docs/test3.md)