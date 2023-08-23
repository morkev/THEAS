# JMARS 3D Visualizer

This software visualizes any surface in the Heliocentric System as long as the dataset has the required parameters. Users can effortlessly navigate and manipulate a 3D graph of any specific region of their interest, zoom in to observe minute details, rotate the view to gain new perspectives and get more insight about the latitude, longitude, elevation and if needed, they can generate the shortest path based on terrain or slope elevation. Datasets were provided by NASA Java Mission-planning and Analysis for Remote Sensing (JMARS).

<b>Developed by</b>: Kevin Mora (student researcher at NASA L'SPACE).

## Installation and Dependencies
```python
pip install numpy
pip install matplotlib
pip install --upgrade matplotlib

Run the following command:
>>> import mpl_toolkits

pip install -U scipy
pip install tqdm
```

```r
NOTE: Last two are not required, but recommended in order to use
additional features from "spicy" (such as cdist, dijkstra and
csr_matrix). Finally, the only usage of "tqdm" is trange.
```

## Obtaining the Datasets
In JMARS, navigate to the region of your interest. Now, go to "Add a Polygon" and click once around the area you would like to export and visualize. The end result should be a red polygon surrounding the area of your interest.

After that, do the following:
```r
Right click on the surface
--> 
Go to: Polygon Functions
--> 
Click on: Export Pixels Data for Polygon
```

A little window called "Pixel Data CSV Export" will appear. Now do the following:
```r
Uncheck :: Pixel ID
Check :: Latitude
Check :: Longitude

Click now on "Add Source" and select the dataset for the body you are working with.

Leave Sampling PPD with the default value.

e.g., "if you are working with a crater such as Occator in
Ceres, then you shall select the Occator crater dataset"
```

Click on "Select File" to choose where to save the file and give it a name. Press the "save" button to complete this operation. Congratulations, you now have the dataset for the selected area.

## Usage
- Install all libraries and dependencies.
- Add your dataset to the "resources" folder.
- In line 6 of class "graph-visualizer.py", instantiate the name of the dataset you just added.
  - Should look like this: filename = "occator.csv"
- Run class "graph-visualizer.py".
