import csv
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial.distance import cdist

# The Floyd-Warshall Algorithm finds the shortest path between
# all pairs of vertices in a weighted graph.
# This class is incomplete and needs some love.

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

# Calculate the pairwise distances between points
distances = cdist(
    np.vstack((latitude_list, longitude_list)).T,
    np.vstack((latitude_list, longitude_list)).T
)

# Connect the nearest points from top to bottom
current_index = 0  # Index of the top point
path = [current_index]

while current_index != len(latitude_list) - 1:
    nearest_index = np.argmin(distances[current_index])
    current_index = nearest_index
    path.append(current_index)
    distances[:, current_index] = np.inf

# Extract the coordinates of the shortest path
shortest_path_latitude = latitude_list[path]
shortest_path_longitude = longitude_list[path]
shortest_path_altitude = altitude_list[path]

# Create the 3D plot with larger size
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the coordinates with gradient effect based on altitude
sc = ax.scatter(latitude_list, longitude_list, altitude_list,
                c=altitude_list, cmap='viridis')

# Plot the shortest path in red
ax.plot(shortest_path_latitude, shortest_path_longitude,
        shortest_path_altitude, 'r')

# Set labels for each axis
ax.set_xlabel('Latitude')
ax.set_ylabel('Longitude')
ax.set_zlabel('Altitude')

# Add a colorbar and adjust its position
cbar = fig.colorbar(sc, pad=0.15)  # Adjust the pad value as needed

# Show the plot
plt.show()
