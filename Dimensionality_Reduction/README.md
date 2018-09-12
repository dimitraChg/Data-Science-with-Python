In this folder you will find two files the FactorAnalysis.ipynb and the PCA.ipunb.
The first file shows how to use the factor analysis algorithm in order to find these factors of the dataset that hold almost 
the most information of the data.
# Factor Analysis
Factor Analysis is a useful tool for investigating special relationships between variables. It allows us to investigate concepts 
that are not easily measured directly by collapsing a large number of variables into a few interpretable underlying factors.
In this section you will see how to apply Factor Analysis in the iris dataset. The factors are independent with each other.
The results are shown below:
![9](https://user-images.githubusercontent.com/42813996/45451735-a4e3ee80-b6e4-11e8-8cfa-311793f569b6.PNG)
We see that for every variable the algorithm create four factors. These factors are the new variables that hold the most 
information of the data and we can use them for extra analysis later.

The second file shows how to find the most important factors of the iris dataset.
# Principal Component Analysis (PCA)
The PCA is used for dimension reduction of a dataset, by finding the most important factors. These factors are independent with each 
other but they are correlated with the variables as you will see below by the heatmap graph. First we gonna see the principal components 
that the algorithm calculated for the variables.
The results are shown below:
![10](https://user-images.githubusercontent.com/42813996/45451927-32274300-b6e5-11e8-829c-746c05b0b065.PNG)
We have four components for every variable in tha dataset.
Next we gonna see the attribute explained_variance_ratio that shows us how much variance is explained by the components we were found. In 
other words that ratio tells us how much information is compressed into the first few components. Also, we see the 
cumulative_variance_ratio that shows the cumulative percentage of the expained variance by the factors. This will help us to figure 
out how many components to keep. In general we make sure that we hold the 70% of the dataset's original information
The results are shown below:
![11](https://user-images.githubusercontent.com/42813996/45453128-9697d180-b6e8-11e8-985a-5b1842faf40d.PNG)
We see that the first component holds the 92.46% of the dataset's variation and the second one holds the 5.30% of the dataset's 
information. So, by keeping the first two components we keep the 97.76% of the information.
Finally, we will see the heatmap diagram that shows as the correlation between the factors we found and the variables we have.
![12](https://user-images.githubusercontent.com/42813996/45455870-41ac8900-b6f1-11e8-8994-fbcc8e533abc.PNG)
We see, that the component 0 is strongly possitively correlated with the variable Petal Length and the component 1 strongly negatively 
correlated with the variable Petal Length.
