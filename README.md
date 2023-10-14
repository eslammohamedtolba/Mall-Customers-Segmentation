# Mall-Customers-Segmentation

This project focuses on segmenting mall customers into distinct groups using the K-means clustering algorithm. 
The primary objective is to gain insights into customer behavior and preferences based on their annual income and spending score.
This README provides an overview of the code, prerequisites, and relevant information.

## Prerequisites
Before running the code, make sure you have the following prerequisites in place:
- Python: You need Python installed on your system. 
- Libraries: You'll need the following Python libraries, which can be installed via pip:
  - Pandas
  - Matplotlib
  - Seaborn
  - Scikit-Learn
You can install these libraries using the following commands: pip install pandas matplotlib seaborn scikit-learn


## Code Overview
The code follows the standard procedure for K-means clustering and customer segmentation. Here's a high-level overview of the code:
- Import required Python libraries, including Pandas, Matplotlib, Seaborn, and Scikit-Learn's KMeans.
- Load the "Mall_Customers.csv" dataset using Pandas and display some basic information about the dataset.
- Check for any missing (none) values in the dataset to decide whether data cleaning is required.
- Visualize the distributions of the "Spending Score (1-100)" and "Annual Income (k$)" columns using Seaborn.
- Create the input data by selecting the "Annual Income (k$)" and "Spending Score (1-100)" columns.
- Find the optimal number of clusters (k) using the "Elbow Method" by calculating the within-cluster sum of squares (WCSS).
- Apply the K-means algorithm with the optimal number of clusters and fit the data to the model.
- Display the cost value (inertia) after clustering and obtain cluster labels and centers.
- Plot the clusters with the data points and centroids using Matplotlib.

## Cost Value
The cost value (inertia) after clustering the dataset is approximately 44448.46.


## Contribution
Contributions to this project are welcome. If you would like to make improvements, add features, or fix issues, feel free to create a pull request. 
Your contributions help enhance this project and make it more valuable to the community.


