from src.data_loader import load_data
from src.clustering import perform_clustering
from src.profiling import cluster_profile
from src.pca_visualization import apply_pca
from src.utils import (
    save_elbow_plot,
    plot_clusters,
    plot_pca
)

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

import pandas as pd

print("Loading dataset...")

df = load_data(
    "dataset/Mall_Customers.csv"
)

features = df[
    [
        "Age",
        "Annual Income (k$)",
        "Spending Score (1-100)"
    ]
]

scaler = StandardScaler()

scaled = scaler.fit_transform(features)

# Elbow Method

wcss = []

for i in range(1,11):

    km = KMeans(
        n_clusters=i,
        random_state=42
    )

    km.fit(scaled)

    wcss.append(
        km.inertia_
    )

save_elbow_plot(wcss)

# Clustering

df, scaled_data, model = perform_clustering(df)

# Cluster Summary

summary = cluster_profile(df)

summary.to_csv(
    "outputs/cluster_summary.csv"
)

# PCA

reduced = apply_pca(
    scaled_data
)

plot_pca(
    reduced,
    df["Cluster"]
)

plot_clusters(df)

df.to_csv(
    "outputs/segmented_customers.csv",
    index=False
)

print("Project completed successfully.")