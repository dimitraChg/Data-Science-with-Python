In this folder there are three files: HierarchicalClustering.ipynb, K-MeansClustering.ipynb and K-NN_Classification.ipynb.
In the first file you will see how to apply Hierarchical Clustering in cars data and produce a dendrogram from them. The results 
are shown below:
# Hierarchical Clulstering

Hierarchical Clustering is an unsupervised machine learning method that is used to predict subgroups within the data based on 
the distance between each data point and its nearest neighbor. Each data point is linked with its neighbor that is most nearby
according to the distance metric. At file HierarchicalClustering.ipynb you see the dendrogram produced by the data that shows 
the taxonomies, the lineages and the relatedness of them.

In the picture below you will see the dendrogram with y-axis represents the distance between the cluster's
centers and x-axis represents the number of the clusters. There are two horizontal lines y=500 and y=150, that intersect the
dendrogram and that means at distance 150 we have five clusters and at distance 500 we have only two.
![1](https://user-images.githubusercontent.com/42813996/45373889-2f4f2400-b5f9-11e8-813e-f455eaf214c5.PNG)

Our target variable is the am variable for the transmition type of any car. The label 0 denotes that the car has automatic 
transmission and label 1 denotes the manual transmission. So, in the above picture we see that the maximun distance in which we 
have two clusters (the same number with the variable's categories) must be greater than 400. For the same reason we keep the 
distance at y=500.

Below, we see the scatter plot of the variables mpg (miles per gallon) and disp (displacement) that shows the two groups 
produced  by the hierarchical clusterng.
![2](https://user-images.githubusercontent.com/42813996/45377254-b5239d00-b602-11e8-9398-f6934c7dbc46.PNG)

The blue one is the cluster 0 that denotes that the car has automatic transmission and the red one is the cluster 1 for the 
manual transmission.

The accuracy of the model is 0.78125 which is a pretty good number and denotes that the model performs well to the data.
![3](https://user-images.githubusercontent.com/42813996/45377725-0aac7980-b604-11e8-92a4-811abb33d17d.PNG)

In the second file you will see how to aplly the K-Means Clustering in iris data. The results are shown below:
# K-Means Clustering
K-Means clustering algorithm is a simple unsupervised algorithm that is used to quickly predict groups from within an unlabeled 
dataset.
At file K-MeansClustering.ipynb you will see how to apply the K-Means clustering to the iris data. Our target variable is the 
species which has three types setosa, versicolor and virginica. Also, we are going to compare the clusters that we found with 
the K-Means Clustering and the truth clusters of the data. This comparison is shown to the scatter plot below:
![4](https://user-images.githubusercontent.com/42813996/45384686-5b799d80-b617-11e8-81ef-fb1371f60657.PNG)

We see above that the clusters are not labeled correct and we need to relabel them. So, the picture below shows exactly that:
![5](https://user-images.githubusercontent.com/42813996/45386461-186df900-b61c-11e8-8279-edb421b3102b.PNG)

Now, that we have the correct labels to the clusters we see that the K-Means algorithm grouped the data pretty close to the 
truth types.
Finally, we print the report of the model to see if it fits well to the data. There are two important measures, the precision 
and the recall. The precision shows the model's relevancy and the recall shows the model's completeness. We need high precision 
and high recall in order to have high accuracy of the model. The results are shown below:
![6](https://user-images.githubusercontent.com/42813996/45388144-ced3dd00-b620-11e8-888c-1cc485e692bb.PNG)

We observe that under the precision return for the record 0  for all points predicted to have a 0 label 100% of the retrieved 
instances were relevant (this is indicated from the value 1.0). The total return shows us that, of the entire dataset, 83% of 
the results that were returned, were trully relevant.

In the K-NN_Classification.ipynb file you will see how to apply the K-NN Classification to the cars data and the accuracy result 
of the model. The results are shown below:
# K-Nearest Neighbor Classification
K-NN Classification is a supervised machine learning method that is used to classify instances based on the arithmetic 
difference between features in a labeled dataset. Our prediction is based on on the am target variable which has two types for 
automatic or manual transmission. The data we are going to use in order to predict the am variable are the variables of mpg 
(miles per gallon), disp (displecement), hp (gross horsepower) and wt (weight). At the picture below you will see the 
application of K-NN to the data:
![7](https://user-images.githubusercontent.com/42813996/45421286-3c215580-b695-11e8-8772-a12f084d3ccb.PNG)

And at the picture that follows you will see the accuracy score of the model, that is how well the K-NN algorithm fits to the 
data:
![8](https://user-images.githubusercontent.com/42813996/45421455-bfdb4200-b695-11e8-8cf7-98905bc64607.PNG)
We observe that at the total return under the precision we have 0.87 that means that of the entire dataset, 87% of 
the results that were returned, were trully relevant.
