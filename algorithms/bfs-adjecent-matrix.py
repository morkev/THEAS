import csv
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from queue import PriorityQueue

filename = "resources/ahuna-mons.csv"

# Use NumPy arrays instead of Python lists
latitude_list = np.array([])
longitude_list = np.array([])
altitude_list = np.array([])

# This class was left as an exercise for the reader
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

# Define the adjacency matrix for the points
num_points = len(latitude_list)
adjacency_matrix = np.zeros((num_points, num_points))

# Calculate the distances between points and update the adjacency matrix
for i in range(num_points):
    for j in range(num_points):
        if i != j:
            distance = np.sqrt((latitude_list[i] - latitude_list[j]) ** 2 +
                               (longitude_list[i] - longitude_list[j]) ** 2 +
                               (altitude_list[i] - altitude_list[j]) ** 2)
            adjacency_matrix[i, j] = distance

# Perform Dijkstra's algorithm
start_index = 0  # Starting point index
end_index = num_points - 1  # Ending point index
distances = np.full(num_points, np.inf)
distances[start_index] = 0
# Store the parent index of each point
parent = np.full(num_points, -1, dtype=int)
visited = np.zeros(num_points, dtype=bool)
queue = PriorityQueue()
queue.put((0, start_index))

while not queue.empty():
    current_distance, current_index = queue.get()
    if current_index == end_index:
        break
    if visited[current_index]:
        continue
    visited[current_index] = True
    for neighbor_index in range(num_points):
        if adjacency_matrix[current_index, neighbor_index] > 0:
            distance = current_distance + \
                adjacency_matrix[current_index, neighbor_index]
            if distance < distances[neighbor_index]:
                distances[neighbor_index] = distance
                parent[neighbor_index] = current_index
                queue.put((distance, neighbor_index))

# Retrieve the shortest path
path_indices = [end_index]
while path_indices[-1] != start_index:
    path_indices.append(parent[path_indices[-1]])
path_indices.reverse()

# Extract the coordinates of the shortest path
path_latitude = latitude_list[path_indices]
path_longitude = longitude_list[path_indices]
path_altitude = altitude_list[path_indices]

# Create the 3D plot with larger size
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the coordinates with gradient effect based on altitude
sc = ax.scatter(latitude_list, longitude_list, altitude_list,
                c=altitude_list, cmap='viridis')

# Plot the shortest path with red lines
ax.plot(path_latitude, path_longitude, path_altitude, 'r')

# Set labels for each axis
ax.set_xlabel('Latitude')
ax.set_ylabel('Longitude')
ax.set_zlabel('Altitude')

# Add a colorbar and adjust its position
cbar = fig.colorbar(sc, pad=0.15)  # Adjust the pad value as needed

# Show the plot
plt.show()
