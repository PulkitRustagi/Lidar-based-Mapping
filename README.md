# Lidar-based-Mapping
Programming a LIDAR onto your computer's mouse pointer to help it map-out an unstructured environment 

### To setup:
You can use a code editor of your choice, but I personally find **PyCharm** very user friendly and easy to use.

### Steps to install **PyCharm** (Ubuntu):
1. Download the tarball .tar.gz from [Here](https://www.jetbrains.com/pycharm/download/#section=linux)
2. Extract the tarball to a directory that supports file execution.For example, if the downloaded version is 1.17.7391, you can extract it to the recommended /opt directory using the following command:
    - `sudo tar -xzf jetbrains-toolbox-1.17.7391.tar.gz -C /`
3. Switch to the bin subdirectory:
    - `cd /opt/pycharm-*/bin`
4. Run pycharm.sh from the bin subdirectory:
    - `./pycharm.sh`

### Clone the Repository files:
1. Go to your workspace (any folder where you which to maintain this code)
2. Open terminal at that location (Right-Click -> Open in Terminal)
3. Clone the repostory by pasting the following into the opened terminal:
    - `git clone "https://github.com/PulkitRustagi/Lidar-based-Mapping.git"`

## How to operate it:
1. Open terminal (using `Ctrl+Alt+T`)
2. start PyCharm:
    - `~<path_to_PyCharm_folder>/bin/pycharm.sh`
3. Open `main.py` script and run to obtain the following output (default **map1.png**):
<p align="center">
  <img width="800" height="500" src="https://github.com/PulkitRustagi/Lidar-based-Mapping/blob/main/Lidar_sim_with_mouse2.gif">
</p>

## Use your own custom map
1. Draw your own map in paint or photoshopor simply download an image that has a **white background with black lines** on it.
2. Save it as a `.png` file in the `maps` folder in the workspace.
3. Go to `env.py` script and change the map name to your newly added map on `line 9` as shown:
![](https://github.com/PulkitRustagi/Lidar-based-Mapping/blob/main/change_map.png)
4. Change the dimensions of the map to the dimennsions of your map image, for example if image is **1200 x 600 pixels**, then go in `main.py` to `line 8` and change accrodingle as shown(in the order (width,height)) as shown:
![](https://github.com/PulkitRustagi/Lidar-based-Mapping/blob/main/map_dimension_change.png)
5. Now you should be able to do this for your own custom map when you run `main.py` script
