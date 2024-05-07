# Thermal and Elevation Analysis System (THEAS)

Visualizes datasets from NASA Java Mission-planning and Analysis for Remote Sensing (JMARS). Current features include the ability to generate 3D graphs of terrain elevation, heatmaps based on the regolith temperature, thermal imaging representations of the surfaces, shortest paths, and top views of the terrain. The program contains error correction functions for missing data points.

<b>Developed by</b>: Kevin Mora, intern at NASA Goddard Space Flight Center.

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

A little window called `Pixel Data CSV Export` will appear. Now do the following:
```r
Uncheck :: Pixel ID
Check :: Latitude
Check :: Longitude

Click now on "Add Source" and select the desired dataset for the body you are working with.

Leave Sampling PPD with the default value.
```

Click on `Select File` to choose where to save the file and give it a name. Press the `Save` button to complete this operation, and delete the first line of the file. Congratulations, you now have the dataset for the selected area.

## Usage
- Install all the libraries and dependencies.
- Add your dataset to the `datasets` folder.
  - i.e.,: `filename = "datasets/name_of_dataset.csv"`
- Run the desired class using `python class_name.py`.
  - e.g.,:`python topographic-surface.py` gives us the result below.

## Output
![Screenshot 2023-08-22 193436](https://github.com/morkev/jmars-3d-visualizer/assets/83437383/cb63fc43-7999-43af-bfed-597cd581a4f5)
> Ahuna Mons in Ceres represented by THEAS.

![collage](https://github.com/morkev/THEAS/assets/83437383/7de75411-bebb-4e08-bf92-d9ba8525cd2e)
> Sample area from lunar terrain featured to display results of thermal imaging enhancement using an error correction algorithm (left). Initial imaging conditions are displayed on the right, highlighting the significant refinement achieved in the processed data.
