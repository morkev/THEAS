import csv
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# The Floyd-Warshall Algorithm finds the shortest path between
# all pairs of vertices in a weighted graph. This approach is
# applicable to both directed and undirected weighted graphs.
# It does not, however, function for graphs with negative
# cycles (the total of the edges in a cycle is negative).


def floyd_warshall(distance_matrix):
    n = len(distance_matrix)
    dist = np.copy(distance_matrix)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i, j] = min(dist[i, j], dist[i, k] + dist[k, j])

    return dist


filename = "resources/ahuna-mons.csv"

# Use NumPy arrays instead of Python lists
latitude_list = np.array([])
longitude_list = np.array([])
altitude_list = np.array([])

with open(filename, "r") as file:
    csv_reader = csv.reader(file)

    # Skip the header row if it exists
    header = next(csv_reader, None)

    # Use generator expressions to yield the values
    latitude_list = np.fromiter(
        (float(row[0]) for row in csv_reader), dtype=float)
    file.seek(0)  # Reset the file pointer
    next(csv_reader, None)  # Skip the header row again
    longitude_list = np.fromiter(
        (float(row[1]) for row in csv_reader), dtype=float)
    file.seek(0)  # Reset the file pointer
    next(csv_reader, None)  # Skip the header row again
    altitude_list = np.fromiter(
        (float(row[2]) for row in csv_reader), dtype=float)

# Create the 3D plot with larger size
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the coordinates with gradient effect based on altitude
sc = ax.scatter(latitude_list, longitude_list, altitude_list,
                c=altitude_list, cmap='viridis')

# Compute the distance matrix using Euclidean distance
coordinates = np.column_stack((latitude_list, longitude_list, altitude_list))
dist_matrix = np.linalg.norm(coordinates[:, np.newaxis] - coordinates, axis=-1)

# Run the Floyd-Warshall algorithm to compute the shortest distances
shortest_distances = floyd_warshall(dist_matrix)

# Find the shortest path from top to bottom
start_index = 0
end_index = len(shortest_distances) - 1
shortest_path = [start_index]
while shortest_path[-1] != end_index:
    current_node = shortest_path[-1]
    # Choose the next node with the minimum distance
    next_node = np.argmin(shortest_distances[current_node])
    shortest_path.append(next_node)

# Convert indices to corresponding latitude, longitude, and altitude values
shortest_path_latitudes = latitude_list[shortest_path]
shortest_path_longitudes = longitude_list[shortest_path]
shortest_path_altitudes = altitude_list[shortest_path]

# Plot the shortest path
ax.plot(shortest_path_latitudes, shortest_path_longitudes,
        shortest_path_altitudes, 'r--')

# Set labels for each axis
ax.set_xlabel('Latitude')
ax.set_ylabel('Longitude')
ax.set_zlabel('Altitude')

# Add a colorbar and adjust its position
cbar = fig.colorbar(sc, pad=0.15)  # Adjust the pad value as needed

# Show the plot
plt.show()
