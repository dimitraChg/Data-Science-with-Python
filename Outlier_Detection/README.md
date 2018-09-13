In this folder you will find three files: the DBSCAN_Clustering.ipynb, the MultivariateMethod.ipynb and the TukeyMethod.ipynb.
Below you will see the results of these files:
In the first file DBSCAN_Clustering.ipynb you will see how to use the DBSCAN clustering in order to identify the outliers.
# DBSCAN Clustering
In this file you will see how to apply the DBSCAN at the iris dataset and the way of working in order to identify the extreme 
values of all variables for every type of the target variable species. First, we gonna see the application of the DBSCAN model 
to the iris dataset with species as the target value. The results are shown below:
![13](https://user-images.githubusercontent.com/42813996/45456410-512cd180-b6f3-11e8-997d-f6f3ba88c906.PNG)
Next we see the labels that the model produced by the data we passed in. The label -1 denotes the extreme values that exist in the
dataset.
![14](https://user-images.githubusercontent.com/42813996/45456564-f5af1380-b6f3-11e8-9ab5-bf90d1325776.PNG)
We see that 6 values have the label -1. So,  we assume that these may be outlies.
In order to see which are these outliers we print the recordings of the dataset that has the label -1.
![16](https://user-images.githubusercontent.com/42813996/45457014-c13c5700-b6f5-11e8-8710-ea27912eb4cb.PNG)
Also, we created a scatter plot of the variables Petal Length and Sepal Width and mark the outlier with black color.
![15](https://user-images.githubusercontent.com/42813996/45456789-bdf49b80-b6f4-11e8-81e2-ad5a8a9e15e5.PNG)

In the second file MultivariateMethod.ipynb you will see how to identify the outliers of multiple dimension variables.
# Multivariate Method
Outliers are the values of a variable that are not too close with the majority of the others values. So, the multivariate method 
of identifying the extremes these values is done through the multiple boxplots and scatter matrices that color the 
different types of the variable with different colors. The first diagram that we will see is the boxplot as shown in the picture 
below:
![17](https://user-images.githubusercontent.com/42813996/45457126-390a8180-b6f6-11e8-91d9-94a40a60969c.PNG)
We see that the target variable is the species (it has three types: setosa, versicolor and virginica) of iris's flowers and the 
variable that we want to see if it has outliers is the sepal length. Also, we observe that the variable sepal length for the 
type virginica has one extreme value under the value of 50.

In the next diagram we gonna see the scatter matrix we produced by all the variables with the target variable to be the 
species. 
The picture below shows the histograms and the scatter plots for all variables in the dataset iris.


![18](https://user-images.githubusercontent.com/42813996/45457244-b3d39c80-b6f6-11e8-8d4d-9eaceb7edab4.PNG)

We observe at the results that for the sepal length variable and the type virginica (represented by blue color) there is a value 
that does not fit with the others.

Finally in the third file TukeyMethod.ipynb, we see the Tukey Method of how to identify the outliers.
# Tukey Method
Tukey Method is an univariate method to identify the extreme values. First, we see the boxplots that we create for all the 
variables.
![19](https://user-images.githubusercontent.com/42813996/45457842-83413200-b6f9-11e8-94d7-b4b52f5aaa70.PNG)

We see that the variable Sepal Width has four extreme values.
Next, we print the outliers of the Sepal Width variable in order to see in which row they exist.

![20](https://user-images.githubusercontent.com/42813996/45458047-81c43980-b6fa-11e8-8f9e-6d2be15b05bc.PNG)

Finally, we use the Tukey method by hand in order to identify the extreme values as it is shown below:
![21](https://user-images.githubusercontent.com/42813996/45482884-e5c91b00-b757-11e8-9203-38b9dd32761d.PNG)
First, we print out some predictive statistics of the data (such as mean, median (Q2), standard deviation (std), minimum value,
maximum value, first quartile (Q1) and third quartile(Q3). Next, we calculate the IQR (Inner Quartile Ratio) which is the 
difference between the third and the first quartile and then we calculate the values of a and b as a=Q1-1.5*IQR and
b=Q3+1.5*IQR. After that we compare the minimum value with the a and if min<a then we have outliers. We do the same with the 
maximum value and b and if max>b we assume that there are extreme values.
Again we see the index that these outliers relly on, that is the rows 14, 31, 32 and 59.
