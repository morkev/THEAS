import csv
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial.distance import cdist

# -----------------------------------------------------------------------------
#
# This class does not work as intended. The current path goes
# across all the data points, instead of the nearest ones. The potential 
# solution is to make a Voronoi grid, and then find the nearest, 
# in order to quickly visualize the result with matplotlib.
#
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
#
# Load data from CSV file and extract latitude, longitude, and altitude
#
# -----------------------------------------------------------------------------
filename = "datasets/baby-twins.csv"
data = np.loadtxt(filename, delimiter=',', skiprows=1)
latitude_list = data[:, 0]
longitude_list = data[:, 1]
altitude_list = data[:, 2]

# -----------------------------------------------------------------------------
#
# Calculate the pairwise distances between points using Euclidean distance
#
# -----------------------------------------------------------------------------
distances = cdist(data[:, :2], data[:, :2], 'euclidean')

# -----------------------------------------------------------------------------
#
# Initialize path starting from the first point (index 0) and visited set
#
# -----------------------------------------------------------------------------
path = [0]
current_index = 0
visited = set([current_index])

# -----------------------------------------------------------------------------
#
# Construct the path by finding the nearest unvisited point at each step
#
# -----------------------------------------------------------------------------
while len(visited) < len(data):
    # Ignore visited points by setting their distances to infinity
    distances[current_index, list(visited)] = np.inf
    nearest_index = np.argmin(distances[current_index])
    if nearest_index in visited:
        break
    visited.add(nearest_index)
    path.append(nearest_index)
    current_index = nearest_index

# -----------------------------------------------------------------------------
#
# Extract the coordinates of the shortest path and create the 3D plot
#
# -----------------------------------------------------------------------------
shortest_path_latitude = latitude_list[path]
shortest_path_longitude = longitude_list[path]
shortest_path_altitude = altitude_list[path]
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# -----------------------------------------------------------------------------
#
# Plot the points and the path 
#
# -----------------------------------------------------------------------------
sc = ax.scatter(latitude_list, longitude_list, altitude_list, c=altitude_list, cmap='viridis')
ax.plot(shortest_path_latitude, shortest_path_longitude, shortest_path_altitude, 'r-', label='Path')

# -----------------------------------------------------------------------------
#
# Set axis labels, and add a color bar and legend
#
# -----------------------------------------------------------------------------
ax.set_xlabel('Latitude')
ax.set_ylabel('Longitude')
ax.set_zlabel('Altitude')
fig.colorbar(sc, pad=0.15)
ax.legend()

plt.show()
