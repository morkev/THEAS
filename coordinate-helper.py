import csv
import math


def convert_to_xyz(latitude, longitude, radius):
    # Convert latitude and longitude to radians
    lat_rad = math.radians(latitude)
    lon_rad = math.radians(longitude)

    # Calculate x, y, z coordinates
    x = radius * math.cos(lat_rad) * math.cos(lon_rad)
    y = radius * math.cos(lat_rad) * math.sin(lon_rad)
    z = radius * math.sin(lat_rad)

    return x, y, z


# Read longitude and latitude from input.csv
csv_filename = "resources/ahuna-mons.csv"
data = []

with open(csv_filename, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        longitude = float(row[0])
        latitude = float(row[1])
        data.append([longitude, latitude])

# Convert coordinates and write to r.csv
# This class was left in case is relevant to certain use cases
radius = 1  # Radius of the sphere (you can adjust this value as needed)
output_filename = "r.csv"
output_data = []

for row in data:
    longitude, latitude = row
    x, y, z = convert_to_xyz(latitude, longitude, radius)
    output_data.append([x, y, z])

with open(output_filename, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(output_data)

print(f"CSV file '{output_filename}' created successfully.")
