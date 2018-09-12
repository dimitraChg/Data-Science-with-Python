In this folder you will find two files the FactorAnalysis.ipynb and the PCA.ipunb.
The first file shows how to use the factor analysis algorithm in order to find these factors of the dataset that hold almost 
the most information of the data.
# Factor Analysis
Factor Analysis is a useful tool for investigating special relationships between variables. It allows us to investigate concepts 
that are not easily measured directly by collapsing a large number of variables into a few interpretable underlying factors.
In this section you will see how to apply Factor Analysis in the iris dataset. The factors are independent with each other.
The results are shown below:


We see that for every variable the algorithm create four factors. These factors are the new variables that hold the most 
information of the data and we can use them for extra analysis later.

The second file shows how to find the most important factors of the iris dataset. These factors have up to 90% of the information 
in the dataset.
# Principal Component Analysis (PCA)
The PCA is used for dimension reduction of a dataset, by finding the most important factors that hold up to 90% of the information 
(also known as variance) of the dataset. These factors are independent with each other but they are correlated with the variables 
as you will see below by the heatmap graph. The results are shown below:


