import math
from collections import namedtuple
import pandas as pd
# from clustering import generate_balanced_clusters
from distance_matrix_generator import haversine_distance, eucledian_distance

# Define a named tuple to store the points
Point = namedtuple("Point", ['x', 'y'])

# Define a function to calculate the Euclidean distance between two points


def length(point1, point2):
    return math.sqrt((point1.lat - point2.lat)**2 + (point1.lon - point2.lon)**2)

# Greedy algorithm to solve the TSP


def greedy(p):
    n = len(p)
    visited = [False] * n
    visited[0] = True
    path = [0]
    # Append the nearest point to the last point in the path
    for i in range(1, n):
        minDist = float('inf')
        minIndex = -1
        for j in range(1, n):
            if not visited[j]:
                d = length(p[path[-1]], p[j])
                if d < minDist:
                    minDist = d
                    minIndex = j
        path.append(minIndex)
        visited[minIndex] = True
    return path

# Another greedy algorithm to solve the TSP


def betterGreedy(p, cluster=[]):
    n = len(p)
    visited = [False] * n
    # Choose the point that is closest to the center of the cluster as the starting point
    pontoCentral = ponto_central(p)
    pontoInicial = 0
    mediaDistAtual = float('inf')
    for i in cluster:
        if length(pontoCentral, p[i]) < mediaDistAtual:
            pontoInicial = i
            mediaDistAtual = length(pontoCentral, p[i])
    visited[pontoInicial] = True
    path = [pontoInicial]

    # Append the nearest point to the last point in the path
    for i in cluster:
        minDist = float('inf')
        minIndex = -1
        for j in cluster:
            if not visited[j]:
                d = length(p[path[-1]], p[j])
                if d < minDist:
                    minDist = d
                    minIndex = j
        if minIndex != -1:
            path.append(minIndex)
            visited[minIndex] = True
    return path

# Function to improve the solution


def Improve(p, path):
    changed = True
    bestIterationPath = path
    bestIterationDist = totalDist(p, path)
    stopper = 0
    # Iterate until the solution does not change or the stopper reaches 10
    while changed and stopper < 10:
        stopper += 1
        print("Iteration: ", stopper)
        changed = False
        for i in range(len(p) - 1):
            for j in range(len(p) - 1):
                if i != j:
                    newPath = swap(path, i, j)
                    if totalDist(p, newPath) < bestIterationDist:
                        path = newPath
                        bestIterationPath = newPath
                        bestIterationDist = totalDist(p, bestIterationPath)
                        changed = True
                        print("changed")
                        print("objAtual: ", bestIterationDist)
    return bestIterationPath

# Function to improve the solution using a 2-opt heuristic


def twoOpt(p, path, maxIterations=float('inf')):
    changed = True
    bestIterationPath = path
    bestIterationDist = totalDist(p, path)
    iteration = 0

    # Iterate until the solution does not change or the maximum number of iterations is reached
    while changed and iteration < maxIterations:
        iteration += 1
        print("Iteration: ", iteration)
        changed = False
        for i in range(1, len(p) - 1):
            for j in range(1, len(p) - 1):
                if i != j:
                    newPath = path[:]
                    newPath[i:j] = path[j-1:i-1:-1]
                    if totalDist(p, newPath) < bestIterationDist:
                        path = newPath
                        bestIterationPath = newPath
                        bestIterationDist = totalDist(p, bestIterationPath)
                        changed = True
                        print("changed")
                        print("objAtual: ", bestIterationDist)
    return bestIterationPath

# Function to calculate the central point of a set of points


def ponto_central(pontos):
    soma_x = sum(p.lat for p in pontos)
    soma_y = sum(p.lon for p in pontos)
    media_x = soma_x / len(pontos)
    media_y = soma_y / len(pontos)
    return Point(media_x, media_y)

# Function to swap two elements in a list


def swap(path, i, j):
    new_path = path[:]
    new_path[i], new_path[j] = new_path[j], new_path[i]
    return new_path

# Function to calculate the total distance of a path


def totalDist(p, path):
    total_distancia = 0
    for i in range(len(path) - 1):
        ponto_atual = p[path[i]]
        proximo_ponto = p[path[i + 1]]
        total_distancia += haversine_distance(ponto_atual, proximo_ponto)
    total_distancia += haversine_distance(p[path[-1]], p[path[0]])
    return total_distancia

# Function to show the data


def show(data, c):
    if c == 0:
        for i in range(len(data)):
            print(data[i])


if __name__ == "__main__":
    # Read the data and run the cluster algorithm
    days = 22
    hours_per_day = 6
    velocity = 5
    reading_velocity = 1.2

    directory = 'storage/dados.csv'
    df = pd.read_csv(directory, delimiter=';')
    points = df[['LATITUDE', 'LONGITUDE']].values

    # Store the clusters in the clusterList variable
    clustersList = generate_balanced_clusters(
        directory, days, hours_per_day, velocity, reading_velocity)
    print("points: ", points)
    # show(clustersList, 0)

    # Store the clusters in a csv file
    clusters = [[] for _ in range(len(set(clustersList["clusters"])))]
    for j in range(len(clustersList["clusters"])):
        cluster_index = clustersList["clusters"][j]
        clusters[cluster_index].append(j)

    clusters_df = pd.DataFrame({'Cluster': [f'Cluster {i}' for i in range(len(clusters))],
                                'Data': clusters})
    clusters_df.to_csv('storage/clusters.csv', index=False)

    counter = 0

    # Convert the points to a list of named tuples
    points = [Point(row[0], row[1]) for row in points]

    # Run the optimization algorithm for each cluster
    for cluster in clusters:
        print("Cluster ", counter)
        path = betterGreedy(points, cluster)
        obj = totalDist(points, path)
        print("Initial Distance: ", obj)

        # Store each result in a corresponding csv file
        path_str = ' '.join(map(str, path))
        data = {'Objectives': [obj], 'Path': [path_str]}
        df = pd.DataFrame(data)
        df.to_csv(f'storage/cluster_{counter}.csv', index=False)

        counter += 1
