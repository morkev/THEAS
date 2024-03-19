import csv
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

filename = "datasets/celeste.csv"

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

# Set labels for each axis
ax.set_xlabel('Latitude')
ax.set_ylabel('Longitude')
ax.set_zlabel('Altitude')

# Add a colorbar and adjust its position
cbar = fig.colorbar(sc, pad=0.15)  # Adjust the pad value as needed

# Show the plot
plt.show()
