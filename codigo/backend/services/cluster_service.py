from fastapi import APIRouter, HTTPException, UploadFile, File
from greedy_algorithm.clustering import generate_balanced_clusters
import pandas as pd
import os
import logging

# function to generate clusters
def cluster(file_path, days, hours_per_day, velocity, reading_velocity):
    df = csv_to_df(file_path)

    raw_clusters, clusters = generate_clusters(
        file_path, days, hours_per_day, velocity, reading_velocity)

    clusters_file_path = export_clusters_to_csv(raw_clusters, clusters)
    points_file_path = export_points_to_csv(df)

    return {
        "num_clusters": raw_clusters["num_clusters"],
        "execution_time": raw_clusters["execution_time"],
        "avg_distance": raw_clusters["avg_distance"],
        "calculated_day": raw_clusters["calculated_day"],
        "clusters_file": clusters_file_path,
        "points_file": points_file_path
    }

# function to export points to csv
def export_points_to_csv(df):
    points = df[['LATITUDE', 'LONGITUDE']].values
    points_df = pd.DataFrame(points, columns=['LATITUDE', 'LONGITUDE'])
    points_file_path = 'storage/points_file.csv'
    points_df.to_csv(points_file_path, index=False)
    return points_file_path

# function to export clusters to csv
def export_clusters_to_csv(raw_clusters, clusters):
    clusters_df = pd.DataFrame({'Cluster': [f'Cluster {i}' for i in range(raw_clusters["num_clusters"])],
                                'Data': clusters})
    clusters_file_path = 'storage/clusters.csv'
    clusters_df.to_csv(clusters_file_path, index=False)
    return clusters_file_path

# function to convert csv to dataframe
def csv_to_df(file_path):
    # Verificar se o arquivo não está vazio
    if os.path.getsize(file_path) == 0:
        raise HTTPException(status_code=400, detail="File is empty")

    
    try:
        # read the csv file with ';' delimiter
        df = pd.read_csv(file_path, delimiter=';')
        logging.info(f"DataFrame columns: {df.columns.tolist()}")
        logging.info(f"DataFrame head: {df.head()}")

        return df
    except pd.errors.ParserError:
        logging.error(
            "Failed to parse CSV with ';' delimiter. Please check the file format.")
        raise HTTPException(
            status_code=400, detail="Failed to parse CSV with ';' delimiter. Please check the file format.")

# function to generate clusters
def generate_clusters(file_path, days, hours_per_day, velocity, reading_velocity):

    raw_clusters = generate_balanced_clusters(
        file_path, days, hours_per_day, velocity, reading_velocity)
    logging.info(f"Clustering result: {raw_clusters}")

    # Prepare the clusters for export
    clusters = [[] for _ in range(raw_clusters["num_clusters"])]
    for idx, cluster_id in enumerate(raw_clusters["clusters"]):
        clusters[cluster_id].append(idx)

    return raw_clusters, clusters