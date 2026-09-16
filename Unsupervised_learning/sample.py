
from sklearn.cluster import KMeans
X = [
[10],
[12],
[14],
[50],
[52],
[55]
]
model= KMeans (
n_clusters=2,
random_state=42,
n_init=2
)

model.fit(X)

print("Cluster labels:", model.labels_)
print("Centroids:", model.cluster_centers_)
