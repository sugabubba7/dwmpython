# Importing necessary libraries
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Generating random data points for demonstration
np.random.seed(0)
X = np.random.rand(100, 2)  # 100 data points with 2 features each

# Initializing KMeans with the number of clusters you want to form
kmeans = KMeans(n_clusters=3)

# Fitting the data to the KMeans algorithm
kmeans.fit(X)

# Getting the centroids and labels based on the trained KMeans algorithm
centroids = kmeans.cluster_centers_
labels = kmeans.labels_

# Visualizing the data points and centroids
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.scatter(centroids[:, 0], centroids[:, 1], marker='X', s=200, linewidths=3, color='r')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('KMeans Clustering')
plt.show()