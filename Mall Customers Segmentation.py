# import required modules
import pandas as pd
import matplotlib.pyplot as plt, seaborn as sns
from sklearn.cluster import KMeans



# loading the dataset
Mall_customers_dataset = pd.read_csv("Mall_Customers.csv")
# show the dataset
Mall_customers_dataset.head()
Mall_customers_dataset.tail()
# show the dataset shape
Mall_customers_dataset.shape
# show some statistical info about the dataset
Mall_customers_dataset.describe()

# check about the none(missing) values in the dataset to decide if will make a data cleaning or not
Mall_customers_dataset.isnull().sum()

plt.figure(figsize=(5,5))
# show the distribution of the Spending Score (1-100) column
sns.distplot(Mall_customers_dataset['Spending Score (1-100)'],color='red')
plt.show()
# show the distribution of the Annual Income (k$) column
sns.distplot(Mall_customers_dataset['Annual Income (k$)'],color='red')
plt.show()



# create input without the counter customer id
X = Mall_customers_dataset.iloc[:,[3,4]].values
# show the input after removing the counter
print(X)



# finding the wcss -> within clusters sum of squares
wcss = []
for i in range(1,11):
    KmeansModel = KMeans(n_clusters=i,init='k-means++',random_state=45)
    KmeansModel.fit(X)
    wcss.append(KmeansModel.inertia_)

# plot the elbow graph
plt.figure(figsize=(5,5))
plt.plot(range(1,11),wcss,color='red')
plt.title("The Elbow point graph")
plt.xlabel("The number of clusters")
plt.ylabel("The Cost value")
plt.show()

# the elbow graph has last drop on number of cluster = 5
Optimal_N_cluster = 5
KmeansModel = KMeans(n_clusters=Optimal_N_cluster,init='k-means++',random_state=45)
KmeansModel.fit(X)
# show the cost value
KmeansModel.inertia_
# show the labels of the clusters
KmeansModel.labels_
# show the clusters centers
KmeansModel.cluster_centers_
# show the clusters of samples in the dataset
Y = KmeansModel.predict(X)



# plot five clusters with the points and centroids
plt.figure(figsize=(8,8))
# plot each group alone with its color and points
plt.scatter(X[Y==0,0],X[Y==0,1],c='red',s=50,label='cluster 1')
plt.scatter(X[Y==1,0],X[Y==1,1],c='green',s=50,label='cluster 2')
plt.scatter(X[Y==2,0],X[Y==2,1],c='blue',s=50,label='cluster 3')
plt.scatter(X[Y==3,0],X[Y==3,1],c='yellow',s=50,label='cluster 4')
plt.scatter(X[Y==4,0],X[Y==4,1],c='orange',s=50,label='cluster 5')
# plot the centers of the clusters
plt.scatter(KmeansModel.cluster_centers_[:,0],KmeansModel.cluster_centers_[:,1],s=100,color='black')
plt.title("Customers groups")
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.show()



