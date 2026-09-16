import numpy as np
from sklearn.cluster import KMeans

X1 = [[5], [7], [8], [20], [22], [25]]

initial_centroids1 = np.array([[7], [22]])

model1 = KMeans(
    n_clusters=2,
    init=initial_centroids1,
    n_init=1,
    max_iter=1,
    random_state=42,
)
model1.fit(X1)

print("--- Problem 1 ---")
print("Cluster labels:", model1.labels_)
print("Centroids:", model1.cluster_centers_.flatten())
