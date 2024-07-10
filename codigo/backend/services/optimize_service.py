import logging
import pandas as pd
from greedy_algorithm.pathing import betterGreedy, totalDist, Point

# funcition to load points from file
def load_points_from_file(points_file: str):
    points_df = pd.read_csv(points_file)
    return [Point(row['LATITUDE'], row['LONGITUDE']) for _, row in points_df.iterrows()]

# function to load cluster from file
def load_cluster_from_file(cluster_index: str, clusters_file_path: str):
    clusters_df = pd.read_csv(clusters_file_path)
    clusters = clusters_df['Data'].apply(eval).tolist()
    cluster = clusters[cluster_index]

    return cluster

# function to optimize the path
def optimize(cluster_index: int, clusters_file_path: str, points_file_path: str):
    points = load_points_from_file(points_file_path)
    cluster = load_cluster_from_file(cluster_index, clusters_file_path)

    # Execute the optimization algorithm
    path = betterGreedy(points, cluster)
    obj = totalDist(points, path)
    path_str = ' '.join(map(str, path))

    result = {
        "initial_distance": obj,
        "path": path_str
    }

    logging.info(f"Optimization result: {result}")
    return result
