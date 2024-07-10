# Import necessary libraries
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, MultiPoint
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
import numpy as np

# Function to check if clusters are within the distance limit


def check_cluster_distances(gdf, max_distance_km):
    clusters = gdf['cluster'].unique()
    invalid_clusters = []
    for cluster in clusters:
        if cluster == -1:
            continue  # Ignore noise
        cluster_points = gdf[gdf['cluster'] == cluster].geometry
        if not cluster_points.empty:
            # Calculate maximum distance between cluster points
            points = MultiPoint(cluster_points.values)
            if points.bounds[2] - points.bounds[0] > max_distance_km / 111 or points.bounds[3] - points.bounds[1] > max_distance_km / 111:
                invalid_clusters.append(cluster)
    return invalid_clusters


# Load house data
casas = pd.read_csv('docs/AMOSTRA_TOTAL.csv', delimiter=',')
geometry = [Point(xy) for xy in zip(casas['LONGITUDE'], casas['LATITUDE'])]
gdf_casas = gpd.GeoDataFrame(casas, geometry=geometry)

# Load street shapefile
gdf_ruas = gpd.read_file('docs/3304557_faces_de_logradouros_2021.shp')

# Parameters for DBSCAN
# eps: Approximately 15 km in degrees
eps = 15 / 111  # Approximately 0.135 degrees
min_samples = 5  # Adjust as necessary

# Apply DBSCAN
coords = gdf_casas[['LONGITUDE', 'LATITUDE']].values
db = DBSCAN(eps=eps, min_samples=min_samples).fit(coords)
gdf_casas['cluster'] = db.labels_

# Check created clusters
max_distance_km = 30
invalid_clusters = check_cluster_distances(gdf_casas, max_distance_km)
print("Invalid clusters:", invalid_clusters)

# Visualize the results
fig, ax = plt.subplots(figsize=(10, 10))
gdf_ruas.plot(ax=ax, color='gray', linewidth=0.5)
gdf_casas.plot(ax=ax, column='cluster', cmap='tab20',
               legend=True, markersize=10)
plt.show()
