import pandas as pd  # type: ignore
import geopandas as gpd  # type: ignore
import matplotlib.pyplot as plt  # type: ignore
from sklearn.cluster import KMeans  # type: ignore
from shapely.geometry import LineString, Point  # type: ignore


def contar_ruas_entre_pontos(lat1, long1, lat2, long2, shapefile_path):

    # Load the shapefile file
    dataframe_geoespacial = gpd.read_file(shapefile_path)

    # Define the start and end points based on the provided coordinates
    ponto_inicio = Point(long1, lat1)
    ponto_fim = Point(long2, lat2)

    # Create a line between the two points
    linha = LineString([ponto_inicio, ponto_fim])

    # Check if the line intersects any street
    intersecta_rua = dataframe_geoespacial['geometry'].intersects(linha)

    # Count how many streets the line intersects
    num_ruas = intersecta_rua.sum()

    return num_ruas


# Load the shapefile file
arquivo_shape = "docs/3304557_faces_de_logradouros_2021.shp"
dataframe_geoespacial = gpd.read_file(arquivo_shape)

# Load data from the CSV file
dados_logradouros = pd.read_csv('docs/AMOSTRA_TOTAL.csv', delimiter=';')

# Define the number of clusters
num_clusters = 400

# Apply the KMeans algorithm
kmeans = KMeans(n_clusters=num_clusters).fit(
    dados_logradouros[['LONGITUDE', 'LATITUDE']])
labels = kmeans.labels_

# Add the cluster labels to the data
dados_logradouros['Cluster'] = labels

# Plot the geospatial data
ax = dataframe_geoespacial.plot(figsize=(10, 6))

# Plot the dots for each street, coloring by cluster
scatter = ax.scatter(
    dados_logradouros['LONGITUDE'], dados_logradouros['LATITUDE'], c=dados_logradouros['Cluster'], marker='o')

# Set title and axis labels
ax.set_title('Mapa dos Logradouros com Localização das Casas')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')

# Add a legend
legend1 = ax.legend(*scatter.legend_elements(), title="Clusters")
ax.add_artist(legend1)

# Display the plot
plt.tight_layout()
plt.show()
