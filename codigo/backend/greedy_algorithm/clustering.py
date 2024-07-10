from typing import OrderedDict
from sklearn.cluster import KMeans
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from distance_matrix_generator import *
from pathing import greedy, totalDist
from datetime import datetime
import time

np.random.seed(42)

# Heuristic approach to determine average distance between 2 points in the dataset 
# (computionally effective, not very accurate)
def sample_and_average_distance(points, n_neighbors=5):
    # Convert list of points to a numpy array
    array_points = np.array([[point.lat, point.lon] for point in points])

    # Convert latitude and longitude from degrees to radians for Haversine formula in NearestNeighbors
    array_points[:, 0] = np.radians(array_points[:, 0])  # Convert latitude
    array_points[:, 1] = np.radians(array_points[:, 1])  # Convert longitude

    # Use Nearest Neighbors with Haversine distance
    nbrs = NearestNeighbors(n_neighbors=n_neighbors, algorithm='auto', metric='haversine')
    nbrs.fit(array_points)
    distances, _ = nbrs.kneighbors(array_points)

    # Convert distances from radians to kilometers (Earth's radius is approximately 6371 kilometers)
    distances *= 6371

    # Compute average distance of the (n_neighbors-1) closest points
    average_distance = np.mean(distances[:, 1:])
    return average_distance

# Estimates the maximum distance that a worker can travel in a month
def max_monthly_distance_and_points(days, hours_per_day, velocity, reading_velocity_minutes, average_distance):
    # Total work hours available in the month
    monthly_hours = days * hours_per_day
    
    reading_velocity_hours = reading_velocity_minutes / 60

    # Calculate the total hours required for traveling one average distance
    travel_time_per_distance = average_distance / velocity  # in hours

    # Assume the maximum number of points a worker can visit is limited by the time available,
    # the total time per point is the sum of travel time and reading time
    total_time_per_point = travel_time_per_distance + reading_velocity_hours

    # Calculate maximum points that can be visited within the available hours
    max_points = int(monthly_hours / total_time_per_point)
    max_points *= 0.94 # Ensure that clusters can be traversed in a feasible time

    # Calculate the maximum feasible distance
    # max_points - 1 because the first point does not require travel
    max_distance = (max_points - 1) * average_distance if max_points > 1 else 0

    # print(f"Max feasible distance: {max_distance}")
    # print(f"Max feasible points: {max_points}")
    return max_distance, max_points

def ideal_clusters(feasible_distance, points, average_distance):
    total_distance = len(points) * average_distance
    necessary_readers = math.ceil(total_distance / feasible_distance)
    # print(f"Necessary Readers: {necessary_readers}")
    points = np.array(points)
    return Kmeans(points, necessary_readers)

# clustering problem algorithm Kmeans
def Kmeans(points, nClusters):
    kmeans = KMeans(n_clusters=nClusters)
    kmeans.fit(points)
    labels = kmeans.predict(points)

    # plot_results(kmeans.cluster_centers_, points, labels, 'K-Means Clustering')
    return labels

def plot_results(cluster_centers, points, labels, title): 
    # # ploting the resulting clusters in a map
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 2)
    plt.scatter(points[:, 0], points[:, 1], c=labels, s=50, cmap='viridis')
    plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], s=200, c='red', marker='.', label='Centroids')
    plt.title(title)
    plt.legend()

    plt.show()

def compute_centroids(points, clusters, n_clusters):
    centroids = np.zeros((n_clusters, 2))
    for i in range(n_clusters):
        cluster_points = np.array([[point.lat, point.lon] for point, cluster in zip(points, clusters) if cluster == i])
        centroids[i] = np.mean(cluster_points, axis=0)
    return centroids

def redistribute_points(points, clusters, threshold, iterations):
    count = 0
    n_clusters = len(set(clusters))
    centroids = compute_centroids(points, clusters, n_clusters)

    while count < iterations:
        cluster_sizes = np.bincount(clusters, minlength=n_clusters)
        if max(cluster_sizes) <= threshold:
            break

        # Iterate over all clusters
        for i in range(n_clusters):
            # Only consider overpopulated clusters
            if cluster_sizes[i] > threshold:
                cluster_indices = [index for index, cluster in enumerate(clusters) if cluster == i]
                # Iterate over each point in the cluster
                for point_index in cluster_indices:
                    point = points[point_index]
                    # Calculate distance to all other cluster centroids
                    dist_point_clusters = [eucledian_distance(point, Point(centroid[0], centroid[1])) for centroid in centroids]
                    
                    # Find the nearest valid cluster that is not overpopulated
                    valid_clusters = [(dist, idx) for idx, dist in enumerate(dist_point_clusters) if cluster_sizes[idx] < threshold]
                    if not valid_clusters:
                        continue  # If no valid clusters, skip to next point

                    new_cluster = min(valid_clusters, key=lambda x: x[0])[1]

                    # Reassign if the new cluster is different and under the threshold
                    if clusters[point_index] != new_cluster:
                        clusters[point_index] = new_cluster
                        # Update cluster sizes immediately
                        cluster_sizes[i] -= 1
                        cluster_sizes[new_cluster] += 1
        
        centroids = compute_centroids(points, clusters, n_clusters)

    return clusters

# Main function with the entire clustering logic encapsulated
def generate_balanced_clusters(csv_path, days, hours_per_day, velocity, reading_velocity):
    start_time = time.time()

    df = pd.read_csv(csv_path, delimiter=';')
    points = df[['LATITUDE', 'LONGITUDE']].values
    points = [Point(row[0], row[1]) for row in points]

    average_distance = sample_and_average_distance(points)
    
    max_distance, max_points = max_monthly_distance_and_points(days, hours_per_day, velocity, reading_velocity, average_distance)

    clusters = ideal_clusters(max_distance, points, average_distance)
    # print(generate_tsp_routes(points, clusters, max_points, velocity, reading_velocity))

    # centroids = compute_centroids(points, clusters, len(set(clusters)))
    # plot_results(centroids, np.array(points), clusters, "Redistributed Clustering")
    
    execution_time = time.time() - start_time

    result = {
        "num_clusters": len(set(clusters)),
        "execution_time": execution_time,
        "avg_distance": (average_distance * max_points) / len(set(clusters)),
        "clusters": clusters,
        "calculated_day": datetime.now().strftime("%Y-%m-%d"),  # Data atual
    }

    return result
    # unique, counts = np.unique(clusters, return_counts=True)
    # cluster_sizes = dict(zip(unique, counts))
    # print(cluster_sizes)

def generate_tsp_routes(points, clusters, max_points, velocity, reading_velocity):
    # Group points by cluster
    cluster_dict = {}
    for point, cluster in zip(points, clusters):
        if cluster not in cluster_dict:
            cluster_dict[cluster] = []
        cluster_dict[cluster].append(point)

    min_time = float('inf')
    max_time = 0
    
    # Generate TSP route for each cluster
    tsp_routes = {}
    for cluster, points in cluster_dict.items():
        tsp_route = greedy(points)  
        distance = totalDist(points, tsp_route)
        total_time = distance / velocity + max_points * (reading_velocity / 60)
        
        min_time = min(min_time, total_time)
        max_time = max(max_time, total_time)

        tsp_routes[cluster] = total_time

    print(f'max time: {max_time}\nmin time: {min_time}\n')
    sorted_items = sorted(tsp_routes.items(), key= lambda item: item[1])
    tsp_routes = OrderedDict(sorted_items)
    return tsp_routes

if __name__ == "__main__":
    
    csv_path = 'codigo/backend/greedy_algorithm/docs/AMOSTRA_TOTAL.csv'
    # csv_path = 'codigo/file/dados.csv'
    days = 22
    hours_per_day = 6
    velocity = 5
    reading_velocity = 1
    res = generate_balanced_clusters(csv_path, days, hours_per_day, velocity, reading_velocity)
    print(res)
    
    # unique, counts = np.unique(res["clusters"], return_counts=True)
    # cluster_sizes = dict(zip(unique, counts))
    # print(cluster_sizes)
