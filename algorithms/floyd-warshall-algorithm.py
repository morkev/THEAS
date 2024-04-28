import csv
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# -----------------------------------------------------------------------------
#
# The Floyd-Warshall Algorithm finds the shortest path between
# all pairs of vertices in a weighted graph. This approach is
# applicable to both directed and undirected weighted graphs.
# It does not, however, function for graphs with negative
# cycles (the total of the edges in a cycle is negative).
#
# -----------------------------------------------------------------------------
def floyd_warshall(distance_matrix):
    n = len(distance_matrix)
    dist = np.copy(distance_matrix)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i, j] = min(dist[i, j], dist[i, k] + dist[k, j])

    return dist

# -----------------------------------------------------------------------------
#
# Read the CSV file and store the latitude, longitude, and altitude values
#
# -----------------------------------------------------------------------------
filename = "datasets/celeste.csv"
latitude_list = np.array([])
longitude_list = np.array([])
altitude_list = np.array([])

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
# Plot the 3D scatter plot of the latitude, longitude, and altitude values
#
# -----------------------------------------------------------------------------
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

sc = ax.scatter(latitude_list, longitude_list, altitude_list,
                c=altitude_list, cmap='viridis')

# -----------------------------------------------------------------------------
#
# Compute the distance matrix using Euclidean distance between points
#
# -----------------------------------------------------------------------------
coordinates = np.column_stack((latitude_list, longitude_list, altitude_list))
dist_matrix = np.linalg.norm(coordinates[:, np.newaxis] - coordinates, axis=-1)

# -----------------------------------------------------------------------------
#
# Run the Floyd-Warshall algorithm to compute the shortest distances, and
# find the shortest path from top to bottom using the computed distances
#
# -----------------------------------------------------------------------------
shortest_distances = floyd_warshall(dist_matrix)
start_index = 0
end_index = len(shortest_distances) - 1
shortest_path = [start_index]

while shortest_path[-1] != end_index:
    current_node = shortest_path[-1]
    next_node = np.argmin(shortest_distances[current_node])
    shortest_path.append(next_node)

# -----------------------------------------------------------------------------
#
# Convert indices to corresponding latitude, longitude, and altitude values.
# Set labels for each axis, and add a colorbar and adjust its position 
#
# -----------------------------------------------------------------------------
shortest_path_latitudes = latitude_list[shortest_path]
shortest_path_longitudes = longitude_list[shortest_path]
shortest_path_altitudes = altitude_list[shortest_path]

ax.plot(shortest_path_latitudes, shortest_path_longitudes,
        shortest_path_altitudes, 'r--')

ax.set_xlabel('Latitude')
ax.set_ylabel('Longitude')
ax.set_zlabel('Altitude')
cbar = fig.colorbar(sc, pad=0.15)

plt.show()
