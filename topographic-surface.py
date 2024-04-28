import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import griddata

# -----------------------------------------------------------------------------
#
# Load data from CSV file
#
# -----------------------------------------------------------------------------
my_data = np.genfromtxt('datasets/baby-twins.csv', delimiter=',')

# -----------------------------------------------------------------------------
#
# Handle missing values in the data 
#
# -----------------------------------------------------------------------------
my_data[my_data == 0] = np.nan
my_data = my_data[~np.isnan(my_data).any(axis=1)]

# -----------------------------------------------------------------------------
#
# Extract the coordinates and define grid for interpolation
#
# -----------------------------------------------------------------------------
X = my_data[:, 0]
Y = my_data[:, 1]
Z = my_data[:, 2]
xi = np.linspace(X.min(), X.max(), 100)
yi = np.linspace(Y.min(), Y.max(), 100)

# -----------------------------------------------------------------------------
#
# Interpolate data onto grid using linear method with griddata
#
# -----------------------------------------------------------------------------
zi = griddata((X, Y), Z, (xi[None, :], yi[:, None]), method='linear')

# -----------------------------------------------------------------------------
#
# Create a meshgrid for plotting the 3D surface
#
# -----------------------------------------------------------------------------
xig, yig = np.meshgrid(xi, yi)
fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
surf = ax.plot_surface(xig, yig, zi, cmap='gist_earth', edgecolor='none')

# -----------------------------------------------------------------------------
#
# Add color bar and labels, and set the Z-axis limits based on data range
#
# -----------------------------------------------------------------------------
cbar = fig.colorbar(surf, shrink=0.7, aspect=20, pad=0.2)
cbar.set_label('Elevation (m)')
ax.set_title('3D Surface Plot')
ax.set_xlabel('Latitude', labelpad=15)
ax.set_ylabel('Longitude', labelpad=15)
ax.set_zlabel('Altitude', labelpad=20)
ax.set_zlim(Z.min(), Z.max())

plt.show()
