import pandas as pd
import plotly.express as px
import numpy as np
from scipy.interpolate import griddata

# -----------------------------------------------------------------------------
#
# Read the data from a CSV file
#
# -----------------------------------------------------------------------------
df = pd.read_csv('datasets/temperature.csv', names=['longitude', 'latitude', 'temperature'], header=0)

# -----------------------------------------------------------------------------
#
# Drop any rows with NaN values in the specified columns (lon, lat, temp) 
#
# -----------------------------------------------------------------------------
df.dropna(subset=['longitude', 'latitude', 'temperature'], inplace=True)

# -----------------------------------------------------------------------------
#
# Extract the data from the dataframe 
#
# -----------------------------------------------------------------------------
x, y, z = df['longitude'].values, df['latitude'].values, df['temperature'].values

# -----------------------------------------------------------------------------
#
# Define grid for interpolation
#
# -----------------------------------------------------------------------------
grid_x, grid_y = np.mgrid[df['longitude'].min():df['longitude'].max():1000j, df['latitude'].min():df['latitude'].max():1000j]

# -----------------------------------------------------------------------------
#
# Interpolate data onto grid using linear method with griddata
#
# -----------------------------------------------------------------------------
grid_z = griddata((x, y), z, (grid_x, grid_y), method='linear')

# -----------------------------------------------------------------------------
#
# Create a plotly figure from the interpolated data
#
# -----------------------------------------------------------------------------
fig = px.imshow(grid_z, 
                x=np.linspace(df['longitude'].min(), df['longitude'].max(), grid_z.shape[1]),
                y=np.linspace(df['latitude'].min(), df['latitude'].max(), grid_z.shape[0]),
                labels=dict(x="Longitude", y="Latitude", color="Temperature"),
                origin='lower',
                color_continuous_scale='thermal')  # Using 'thermal' color scale for temperature


# -----------------------------------------------------------------------------
#
# Update layout and show the plot with error correction
#
# -----------------------------------------------------------------------------
fig.update_layout(
    title='Temperature Map',
    xaxis_title='Longitude',
    yaxis_title='Latitude',
    coloraxis_colorbar=dict(title='Temperature')
)

fig.show()
