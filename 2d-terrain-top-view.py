import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from scipy.interpolate import griddata

# -----------------------------------------------------------------------------
#
# Load elevation data from a CSV file
#
# -----------------------------------------------------------------------------
data = np.genfromtxt('datasets/celeste.csv', delimiter=',')

# -----------------------------------------------------------------------------
#
# Extract coordinates and elevation data 
#
# -----------------------------------------------------------------------------
x, y, z = data[:, 0], data[:, 1], data[:, 2]

# -----------------------------------------------------------------------------
#
# Define grid for interpolation, 1000j is the number of points to interpolate
#
# -----------------------------------------------------------------------------
grid_x, grid_y = np.mgrid[min(x):max(x):1000j, min(y):max(y):1000j] 

# -----------------------------------------------------------------------------
#
# Interpolate data onto grid using linear method with griddata
#
# -----------------------------------------------------------------------------
grid_z = griddata((x, y), z, (grid_x, grid_y), method='linear')

# -----------------------------------------------------------------------------
#
# Create a figure and dDisplay the data as an image
#
# -----------------------------------------------------------------------------
fig, ax = plt.subplots()
c = ax.imshow(grid_z.T, extent=(min(x), max(x), min(y), max(y)), origin='lower', cmap=cm.gist_earth)
ax.axis('off')

# -----------------------------------------------------------------------------
#
# Add a color bar and save the plot as a PNG file
#
# -----------------------------------------------------------------------------
cbar = fig.colorbar(c, ax=ax, orientation='vertical', shrink=0.9)
cbar.set_label('Elevation (meters)')
plt.savefig('datasets/2d-terrain-view-top.png', dpi=300, bbox_inches='tight')
plt.show()
