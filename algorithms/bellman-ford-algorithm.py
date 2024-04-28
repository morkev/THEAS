import csv
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

filename = "datasets/ahuna-mons.csv"

# -----------------------------------------------------------------------------
#
# Use NumPy arrays instead of Python lists for the coordinates 
#
# -----------------------------------------------------------------------------
latitude_list = np.array([])
longitude_list = np.array([])
altitude_list = np.array([])

# -----------------------------------------------------------------------------
#
# Read the CSV file and store the latitude, longitude, and altitude values
#
# -----------------------------------------------------------------------------
with open(filename, "r") as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader, None)
    
    latitude_list = np.fromiter(
        (float(row[0]) for row in csv_reader), dtype=float)
    file.seek(0)
    next(csv_reader, None)
    longitude_list = np.fromiter(
        (float(row[1]) for row in csv_reader), dtype=float)
    file.seek(0)
    next(csv_reader, None)
    altitude_list = np.fromiter(
        (float(row[2]) for row in csv_reader), dtype=float)


# -----------------------------------------------------------------------------
#
# Define the Bellman-Ford algorithm function with Delta stepping optimization
#
# -----------------------------------------------------------------------------
def bellman_ford_delta(graph, start, delta):
    num_nodes = len(graph)
    distance = np.full(num_nodes, np.inf)
    distance[start] = 0

    bucket_sizes = int(np.ceil(np.max(altitude_list) / delta)) + 1
    buckets = [[] for _ in range(bucket_sizes)]

    for i in range(num_nodes):
        bucket = int(altitude_list[i] / delta)
        buckets[bucket].append(i)

    for bucket_id in range(bucket_sizes):
        is_updated = False
        for u in range(num_nodes):
            if u not in buckets[bucket_id]:
                continue
            for v in range(num_nodes):
                if distance[u] + graph[u][v] < distance[v]:
                    distance[v] = distance[u] + graph[u][v]
                    is_updated = True
        if not is_updated:
            break

    return distance

# -----------------------------------------------------------------------------
#
# Create the graph based on the latitude, longitude, and altitude lists
#
# -----------------------------------------------------------------------------
num_nodes = len(latitude_list)
graph = np.zeros((num_nodes, num_nodes))

# -----------------------------------------------------------------------------
#
# This function is the purest definition of garbage code
#
# -----------------------------------------------------------------------------
for i in range(num_nodes):
    for j in range(num_nodes):
        if i != j:
            graph[i][j] = np.sqrt(
                (latitude_list[i] - latitude_list[j]) ** 2 +
                (longitude_list[i] - longitude_list[j]) ** 2 +
                (altitude_list[i] - altitude_list[j]) ** 2
            )

# -----------------------------------------------------------------------------
#
# Choose the top node as the starting point, and set the delta value. Then, run
# run the Bellman-Ford algorithm with Delta stepping for the shortest distances
#
# -----------------------------------------------------------------------------
start_node = 0
delta = 100
distances = bellman_ford_delta(graph, start_node, delta)

for i in range(num_nodes):
    print(
        f"Shortest distance from node {start_node} to node {i}: {distances[i]}")

# -----------------------------------------------------------------------------
#
# Create the 3D plot with larger size, and plot the coordinates with gradient effect based on altitude
#
# -----------------------------------------------------------------------------
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
sc = ax.scatter(latitude_list, longitude_list, altitude_list,
                c=altitude_list, cmap='viridis')

# -----------------------------------------------------------------------------
#
# Set labels for each axis, and add a colorbar and adjust its position
#
# -----------------------------------------------------------------------------
ax.set_xlabel('Latitude')
ax.set_ylabel('Longitude')
ax.set_zlabel('Altitude')
cbar = fig.colorbar(sc, pad=0.15)

plt.show()
