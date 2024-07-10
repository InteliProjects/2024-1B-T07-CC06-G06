import time
import random
import math
import numpy as np
import pandas as pd
import folium
from ..backend.greedy_algorithm.clustering import generate_balanced_clusters # Import the function from clustering.py

# Existing functions such as calculate_distance, initialize_population, greedy_algorithm should remain as they are.

def generate_routes_for_clusters(clusters, num_cities, cities, select_size, crossover_rate, mutation_rate, target):
    routes = []
    for cluster_id in set(clusters):
        cluster_points = [index for index, value in enumerate(clusters) if value == cluster_id]
        cluster_cities = {i: cities[i] for i in cluster_points}
        population = initialize_population(len(cluster_cities), 100, cluster_cities)
        best_solution, gen_number, refined_distance = genetic_algorithm(
            population, len(cluster_cities), cluster_cities, select_size, crossover_rate, mutation_rate, target)
        routes.append((best_solution, refined_distance))

def calculate_distance(path, cities):
    """
    @param path: A list of indices representing the order of points to be visited 
    @param cities: Dictionary with points as keys and locations as values, each value is a tuple (x, y)

    @return: Total Euclidean Distance between 2 points
    """
    total_distance = 0
    for i in range(len(path)):
        x1, y1 = cities[path[i]]
        x2, y2 = cities[path[(i + 1) % len(path)]]
        total_distance += math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return total_distance


def initialize_population(num_cities, population_size, cities):
    """
    @param num_cities: Number of points in the problem, used to generate random routes
    @param population_size: Initial population to be created for the algorithm
    @param cities: Dictionary with points as keys and locations as values, each value is a tuple (x, y)

    @return: List of tuples, each containing a fitness value and corresponding route. The fitness is measured by the distance, meaning a smaller distance is a more optimal solution.
    """
    population = []
    num_greedy = int(population_size * 0.2)  # 20% of the initial population will be greedy routes
    for _ in range(num_greedy):
        start_city = random.randint(0, len(cities) - 1)
        greedy_route = greedy_algorithm(cities, start_city)
        fitness = calculate_distance(greedy_route, cities)
        population.append((fitness, greedy_route))

    for _ in range(population_size - num_greedy):
        perm = list(range(num_cities))
        random.shuffle(perm)
        fitness = calculate_distance(perm, cities)
        population.append((fitness, perm))
    return population


# Function to calculate the total distance of a solution
def calculate_total_distance(solution, cities):
    """
    @param solution: List of points indices, representing the travel order
    @param cities: Dictionary with points as keys and locations as values, each value is a tuple (x, y)

    @return: Total distance of the route. Computed by summing the consecutive distances, considers the route circular.
    """
    total_distance = 0
    for i in range(len(solution)):
        index_current_city = solution[i]
        index_next_city = solution[(i + 1) % len(solution)]
        total_distance += calculate_point_distance(index_current_city, index_next_city, cities)
    return total_distance


#calculates distance between two points
def calculate_point_distance(city1_index, city2_index, cities):
    """
    @param city1_index: Point 1 index
    @param city2_index: Point 2 index
    @param cities: Dictionary with points as keys and locations as values, each value is a tuple (x, y)

    @return: Euclidean Distance between the 2 points
    """
    x1, y1 = cities[city1_index]
    x2, y2 = cities[city2_index]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

#greedy algorithm
def greedy_algorithm(cities, start_city):
    """
    @param cities: Dictionary with points as keys and locations as values, each value is a tuple (x, y)
    @param start_city: start point index

    @return: List of indexes of the points to be visited, in order
    """
    if isinstance(start_city, np.ndarray):
        if start_city.size == 1:
            start_city = int(start_city)
        else:
            raise ValueError("start_city is an array with more than one element.")
    elif not isinstance(start_city, int):
        raise ValueError("start_city must be an integer.")

    num_cities = len(cities)
    visited = {i: False for i in range(num_cities)}
    tour = [start_city]
    visited[start_city] = True

    current_city = start_city
    for _ in range(1, num_cities):
        next_city = None
        min_dist = float('inf')
        for i in range(num_cities):
            if not visited[i]:
                dist = calculate_point_distance(current_city, i, cities)
                if dist < min_dist:
                    min_dist = dist
                    next_city = i
        if next_city is not None:
            tour.append(next_city)
            visited[next_city] = True
            current_city = next_city
        else:
            break

    return tour


#formats output

def output_solution(solution, total_distance):
    """
    @param solution: List of point indices to be visited
    @param total_distance: Total distance of the route

    @return: Correct output format
    """
    output_data = f"{total_distance:.2f} 0\n" + ' '.join(map(str, solution))
    print(output_data)
    return output_data


#genetic algorithm
def genetic_algorithm(population, num_cities, cities, select_size, crossover_rate, mutation_rate, target):
    """
    @param population: Initial population of solutions, where each solution is a tuple (distance, route).
    @param num_cities: The number of cities in the route optimization problem.
    @param cities: A dictionary mapping city indices to their coordinates (x, y).
    @param select_size: The number of solutions to consider during the selection phase.
    @param crossover_rate: Probability with which crossover is applied between two selected parents.
    @param mutation_rate: Probability with which mutation is applied to an offspring.
    @param target: Target distance value which, if achieved, stops the algorithm.

    @return: A tuple containing the optimized route, the number of generations processed, and the distance of the refined solution.
    """
    gen_number = 0
    for _ in range(1000):
        new_population = []
        new_population.append(population[0])
        new_population.append(population[1])

        for _ in range(int((len(population) - 2) / 2)):
            if random.random() < crossover_rate:
                parent1 = sorted(random.choices(population, k=select_size))[0]
                parent2 = sorted(random.choices(population, k=select_size))[0]

                point = random.randint(0, num_cities - 1)
                child1 = parent1[1][:point] + [j for j in parent2[1] if j not in parent1[1][:point]]
                child2 = parent2[1][:point] + [j for j in parent1[1] if j not in parent2[1][:point]]
                gen_number += 1

            else:
                child1 = random.choice(population)[1]
                child2 = random.choice(population)[1]

            # Mutation
            if random.random() < mutation_rate:
                point1, point2 = random.sample(range(num_cities), 2)
                child1[point1], child1[point2] = child1[point2], child1[point1]
                child2[point1], child2[point2] = child2[point2], child2[point1]

            new_population.append((calculate_distance(child1, cities), child1))
            new_population.append((calculate_distance(child2, cities), child2))

        population = new_population
        best_solution = sorted(population, key=lambda x: x[0])[0]
        if best_solution[0] < target:
            break

    # Run the greedy algorithm to improve the best solution found
    refined_solution = greedy_algorithm(cities, best_solution[1][0])
    refined_distance = calculate_distance(refined_solution, cities)
    return refined_solution, gen_number, refined_distance


#optimizes route
def two_opt(route, cities):
    """
    Evaluate the execution time of an algorithm.

    Args:
        algorithm: The algorithm function to be evaluated.
        *args: Positional arguments for the algorithm.
        **kwargs: Keyword arguments for the algorithm.

    Returns:
        A dictionary containing the solution and execution time.
    """
    start_time = time.time()
    solution, _, refined_distance = algorithm(*args, **kwargs)
    end_time = time.time()
    execution_time = end_time - start_time

    return {
        'solution': solution,
        'distance': refined_distance,
        'execution_time': execution_time
    }

# Function to draw the map with the best solution
def draw_map(solution, cities):
    """
    @param solution: List of city indices representing the order of the route.
    @param cities: Dictionary mapping city indices to their coordinates (x, y).

    @return: HTML with map of the route
    """
    first_city = cities[solution[0]]
    fmap = folium.Map(location=[first_city[0], first_city[1]], zoom_start=12)
    
    for i in range(len(solution)):
        current_city = solution[i]
        next_city = solution[(i + 1) % len(solution)]
    
        folium.Marker(
            location=[cities[current_city][0], cities[current_city][1]],
            popup=f"City {current_city}"
        ).add_to(fmap)
        
        
        folium.PolyLine(
            locations=[[cities[current_city][0], cities[current_city][1]], 
                       [cities[next_city][0], cities[next_city][1]]],
            color="blue"
        ).add_to(fmap)
    
    fmap.save("route_map.html")
    print("Map saved as route_map.html")

# Example usage
if __name__ == "__main__":
    csv_path = 'codigo\dataset\AMOSTRA_TOTAL.csv'
    days = 22
    hours_per_day = 6
    velocity = 5
    reading_velocity = 2

    cluster_info = generate_balanced_clusters(csv_path, days, hours_per_day, velocity, reading_velocity)
    clusters = cluster_info["clusters"]
    points = cluster_info["points"]
    cities = {i: point for i, point in enumerate(points)}

    select_size = 10  
    crossover_rate = 0.8  
    mutation_rate = 0.05  
    target = 100

    routes = generate_routes_for_clusters(clusters, len(points), cities, select_size, crossover_rate, mutation_rate, target)
    for idx, (route, distance) in enumerate(routes):
        print(f"Route for cluster {idx}: {route} with distance {distance}")
        draw_map(route, cities)
