# Hierarchical Clulstering

Hierarchical Clustering is an unsupervised machine learning method that is used to predict subgroups within the data based on the
distance between each data point and its nearest neighbor. Each data point is linked with its neighbor that is most nearby
according to the distance metric. At file HierarchicalClustering.ipynb you see the dendrogram produced by the data that shows the
taxonomies, the lineages and the relatedness of them.

In the picture below you will see the dendrogram with y-axis represents the distance between the cluster's
centers and x-axis represents the number of the clusters. There are two horizontal lines y=500 and y=150, that intersect the
dendrogram and that means at distance 150 we have five clusters and at distance 500 we have only two.
![1](https://user-images.githubusercontent.com/42813996/45373889-2f4f2400-b5f9-11e8-813e-f455eaf214c5.PNG)

Our target variable is the am variable for the transmition type of any car. The label 1 denotes that the car has automatic 
transmission and label 0 denotes the manual transmission. So, in the above picture we see that the maximun distance in which we 
have two clusters (the same number with the variable's categories) must be greater than 400. For the same reason we keep the 
distance at y=500.

Below, we see the scatter plot of the variables mpg (miles per gallon) and disp (displacement) that shows the two groups produced 
by the hierarchical clusterng.
![2](https://user-images.githubusercontent.com/42813996/45377254-b5239d00-b602-11e8-9398-f6934c7dbc46.PNG)

The blue one is the cluster 1 that denotes that the car has automatic transmission and the red one is the cluster 0 for the manual 
transmission.

The accuracy of the model is 0.78125 which is a pretty good number and denotes that the model performs well to the data.
![3](https://user-images.githubusercontent.com/42813996/45377725-0aac7980-b604-11e8-92a4-811abb33d17d.PNG)
