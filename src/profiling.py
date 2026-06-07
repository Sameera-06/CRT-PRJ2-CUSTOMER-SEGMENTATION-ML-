def cluster_profile(df):

    summary = df.groupby(
        "Cluster"
    ).mean(numeric_only=True)

    return summary