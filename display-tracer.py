import csv
import math
import numpy as np

# This class was deprecated in favor of the NumPy array implementation and dataset structure
# Would be beneficial if there's no instance of Z (altitude) coordinates, in which case the class
# coordinate-helper.py would be used in conjunction with this class in sequentially-dependant order


def load_coordinates_from_csv(file_path):
    coordinates = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            latitude, longitude, altitude = map(float, row)
            coordinates.append((latitude, longitude, altitude))
    return coordinates


def calculate_distance(coord1, coord2):
    lat1, lon1, alt1 = coord1
    lat2, lon2, alt2 = coord2

    radius = 473  # Radius of Ceres in kilometers

    lat1_rad = np.radians(lat1)
    lon1_rad = np.radians(lon1)
    lat2_rad = np.radians(lat2)
    lon2_rad = np.radians(lon2)

    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    a = np.sin(dlat / 2) ** 2 + np.cos(lat1_rad) * \
        np.cos(lat2_rad) * np.sin(dlon / 2) ** 2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))

    distance = radius * c

    return distance


def floyd_warshall(coordinates):
    n = len(coordinates)
    distances = np.full((n, n), np.inf)

    for i in range(n):
        for j in range(n):
            if i == j:
                distances[i, j] = 0
            else:
                distances[i, j] = calculate_distance(
                    coordinates[i], coordinates[j])

    for k in range(n):
        distances = np.minimum(
            distances, distances[:, k].reshape(n, 1) + distances[k, :])

    return distances


# Example usage
csv_file = "resources/ahuna-mons.csv"
coordinates = load_coordinates_from_csv(csv_file)
distances = floyd_warshall(coordinates)

# Print the resulting distances
for row in distances:
    print(row)
