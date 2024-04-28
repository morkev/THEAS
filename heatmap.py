import pandas as pd
import plotly.express as px

# -----------------------------------------------------------------------------
#
# Read the data from a CSV file
#
# -----------------------------------------------------------------------------
df = pd.read_csv('datasets/temperature.csv', names=['latitude', 'longitude', 'regolith_temperature'], header=0)

# -----------------------------------------------------------------------------
#
# Drop any rows with NaN values in the specified columns (lat, lon, temp)
#
# -----------------------------------------------------------------------------
df.dropna(subset=['latitude', 'longitude', 'regolith_temperature'], inplace=True)

# -----------------------------------------------------------------------------
#
# Create the scatter plot with a fixed small marker size and color scale
#
# -----------------------------------------------------------------------------
fig = px.scatter(df, x='longitude', y='latitude', color='regolith_temperature',
                 size_max=5,
                 labels={'regolith_temperature': 'Temperature'},
                 title='Regolith Temperature of Data Points')
# -----------------------------------------------------------------------------
#
# Adjust the marker size and initial zoom level. Add 2% padding.
#
# -----------------------------------------------------------------------------
fig.update_traces(marker=dict(size=15))  # Adjust circle size
lon_pad = (df['longitude'].max() - df['longitude'].min()) * 0.02
lat_pad = (df['latitude'].max() - df['latitude'].min()) * 0.02

# -----------------------------------------------------------------------------
#
# Update layout and show the plot with error correction
#
# -----------------------------------------------------------------------------
fig.update_layout(
    xaxis_title='Longitude',
    yaxis_title='Latitude',
    xaxis_range=[df['longitude'].min() - lon_pad, df['longitude'].max() + lon_pad],
    yaxis_range=[df['latitude'].min() - lat_pad, df['latitude'].max() + lat_pad]
)

fig.show()
