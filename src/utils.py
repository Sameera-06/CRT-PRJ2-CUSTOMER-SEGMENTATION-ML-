import matplotlib.pyplot as plt
import seaborn as sns

def save_elbow_plot(wcss):

    plt.figure(figsize=(8,5))

    plt.plot(
        range(1,11),
        wcss,
        marker='o'
    )

    plt.title("Elbow Method")

    plt.xlabel("Clusters")

    plt.ylabel("WCSS")

    plt.savefig(
        "outputs/elbow_plot.png"
    )

    plt.close()


def plot_clusters(df):

    plt.figure(figsize=(8,6))

    sns.scatterplot(
        x="Annual Income (k$)",
        y="Spending Score (1-100)",
        hue="Cluster",
        data=df,
        palette="Set2"
    )

    plt.savefig(
        "outputs/customer_segments.png"
    )

    plt.close()


def plot_pca(reduced, labels):

    plt.figure(figsize=(8,6))

    plt.scatter(
        reduced[:,0],
        reduced[:,1],
        c=labels
    )

    plt.title("PCA Clusters")

    plt.savefig(
        "outputs/pca_clusters.png"
    )

    plt.close()