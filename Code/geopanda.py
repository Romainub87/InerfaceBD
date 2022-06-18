import geopandas as gp
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame(
    {'City': ['Paris', 'Berlin', 'Copenhague', 'Washington', 'Yamoussoukro',"Beijing","New Delhi"],
     'Country': ['France', 'Germany', 'Denmark', 'United States of America', "Ivory Coast","China","Inde"],
     'Latitude': [48.856613, 52.520008, 55.675758, 38.907192, -26.089149,39.906217,28.613895],
     'Longitude': [2.352222,13.404954, 12.569020, -77.036873, 28.440760,116.391276,77.209006]})
world = gp.read_file(gp.datasets.get_path('naturalearth_lowres'))
gdf = gp.GeoDataFrame(
    df, geometry=gp.points_from_xy(df.Longitude, df.Latitude,),)
print(gdf["G"])
ax = world.plot(
    color='white', edgecolor='black')
gdf.plot(ax=ax, color='red',markersize=10)
plt.show()