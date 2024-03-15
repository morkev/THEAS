# JMARS 3D Visualizer

Visualizes any surface in the from NASA Java Mission-planning and Analysis for Remote Sensing (JMARS), as long as the dataset has the required LAMO parameters. Users can effortlessly navigate and manipulate the 3D graph of any specific region of their interest, zoom in to observe minute details, rotate the view and get more insight about the latitude, longitude, elevation and if needed, they can generate the shortest path based on the terrain or the slope elevation.

<b>Developed by</b>: Kevin Mora.

## Installation and Dependencies
```python
pip install numpy
(if the command above does not work, run: py -3 -m  pip install numpy)
pip install matplotlib
(if the command above does not work, run: py -3 -m  pip install matplotlib)

>>> pip install --upgrade matplotlib
>>> import mpl_toolkits

pip install -U scipy
(py -3 -m  pip install -U scipy)
pip install tqdm
(py -3 -m  pip install tqdm)
```

```r
NOTE: Last two are not required, but recommended in order to use
additional features from "spicy" (such as cdist, dijkstra and
csr_matrix). Finally, the only usage of "tqdm" is trange.
```

## Obtaining the Datasets
In JMARS, navigate to the region of your interest. Now, go to `Add a Polygon` and click once around the area you would like to export and visualize. The end result should be a red polygon surrounding the area you want to visualize.

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

Click now on "Add Source" and select the desired "Elevation" dataset for the body you are working with.

Leave Sampling PPD with the default value.

e.g., "if you are working with a crater such as Occator in
Ceres, then you shall select the Occator crater dataset"
```

Click on `Select File` to choose where to save the file and give it a name. Press the `Save` button to complete this operation. Congratulations, you now have the dataset for the selected area.

## Usage
- Install all the libraries and dependencies.
- Add your dataset to the "datasets" folder.
- In line 6 of class "graph-visualizer.py", instantiate the name of the dataset you just added.
  - Should look like this: filename = "datasets/name_of_dataset.csv"
- Run class "graph-visualizer.py".

## Output
![Screenshot 2023-08-22 193436](https://github.com/morkev/jmars-3d-visualizer/assets/83437383/cb63fc43-7999-43af-bfed-597cd581a4f5)
> Ahuna Mons in Ceres represented by JMARS 3D Visualizer
