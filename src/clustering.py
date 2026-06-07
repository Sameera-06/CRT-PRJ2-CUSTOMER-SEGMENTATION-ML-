from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def perform_clustering(df):

    features = df[
        [
            "Age",
            "Annual Income (k$)",
            "Spending Score (1-100)"
        ]
    ]

    scaler = StandardScaler()

    scaled_data = scaler.fit_transform(features)

    kmeans = KMeans(
        n_clusters=5,
        random_state=42
    )

    df["Cluster"] = kmeans.fit_predict(
        scaled_data
    )

    return df, scaled_data, kmeans