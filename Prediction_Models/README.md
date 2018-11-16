In this folder you will find three files: LinearRegression.ipynb, LogisticRegression.ipynb, NaiveBayes.ipynb. In the first file you
will see how to estimate fall undergraduate enrollments in the enrollment_forecast data. The results are shown below:
# Linear Regression

Linear regression attempts to model the relationship between two or more variables by fitting a linear equation to observed data.
One or more variables are considered to be explanatory variables, and the other is considered to be a dependent variable. Always we
have one dependent variable and one or more explanatory variables. According to this there are two types of Linear Regression the 
simple and the multiple. If we have one explanatory variable we have simple Linear Regression and if we have more than one we have
multiple Linear Regression.

In the picture below we will see the pairplot (histograms and scatter plots in one figure) that we create for every single variable
of the data.

![22](https://user-images.githubusercontent.com/42813996/48647536-f49caa00-e9f4-11e8-952e-4fd6ebbf9556.PNG)

Before attempting to fit a linear model to observed data, we should first determine whether or not there is a relationship between
the variables. So we print out the correlation table to see if there is any relationship betwwen the variables.

![23](https://user-images.githubusercontent.com/42813996/48647798-c23f7c80-e9f5-11e8-808a-efbd96a29200.PNG)

We see that there is no important correlation between the variables unem (unemployment rate) and hgrad (high school graduates).
So, we keep these two variables as explanatory for the regression model.
As dependent variable we set the roll variable (fall undergraduate enrollment), which is shown below:

![24](https://user-images.githubusercontent.com/42813996/48648182-1ac34980-e9f7-11e8-8019-1d0ec43bef59.PNG)

Then, we scale our data as shown below:

![25](https://user-images.githubusercontent.com/42813996/48648350-b0f76f80-e9f7-11e8-9eb9-4f2f4f4b4899.PNG)

And checking for missing values:

![26](https://user-images.githubusercontent.com/42813996/48648395-da180000-e9f7-11e8-8860-47d301d9089f.PNG)

We see that there are no missing values of the data.

Finally, we fit Linear Regression on the data and calculate the R-squared (a statistical measure of how close the data are to 
the fitted regression line) as it is shown below:

![27](https://user-images.githubusercontent.com/42813996/48648619-c15c1a00-e9f8-11e8-99c9-43cdd95580cb.PNG)

We see that the 84.88% of the data are explained from the model.
