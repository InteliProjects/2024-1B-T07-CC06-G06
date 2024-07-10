import math
import pandas as pd
import numpy as np
from collections import namedtuple

Point = namedtuple("Point", ['lat', 'lon'])

def eucledian_distance(point1, point2):
    def convert_to_cartesian(lat, lon):
        R = 6371.0  # Radius of the Earth in kilometers
        lat = R * math.radians(lon) * math.cos(math.radians(lat))
        lon = R * math.radians(lat)
        return Point(lat, lon)

    point1, point2 = convert_to_cartesian(point1.lat, point1.lon), convert_to_cartesian(point2.lat, point2.lon)
    return math.sqrt((point1.lat - point2.lat)**2 + (point1.lon - point2.lon)**2)

# Haversine formula is more accurate, however, more expensive (change based on the problem scale)
def haversine_distance(point1, point2):
    R = 6371.0  # Radius of the Earth in kilometers
    lat1, lon1 = math.radians(point1.lat), math.radians(point1.lon)
    lat2, lon2 = math.radians(point2.lat), math.radians(point2.lon)
    
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    return R * c


# def generate_distance_matrix(data):
#     n = len(data)
#     matrix = np.zeros((n, n)) 
#     for i in range(n):
#         for j in range(n):
#             if i != j:
#                 matrix[i][j] = haversine_distance(data[i], data[j])
#     return matrix


# if __name__ == "__main__":
#     directory = 'codigo/dataset/AMOSTRA_TOTAL.csv'
#     df = pd.read_csv(directory, delimiter=';')
#     points = df[['LATITUDE', 'LONGITUDE']].values
#     points = [convert_to_cartesian(row[0], row[1]) for row in points]
#     pd.DataFrame(generate_distance_matrix(points)).to_csv('distance_matrix.csv', index=False)