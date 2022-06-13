# import netCDF4 as nc
import xarray as xr
xr.open_dataset("C.nc").to_dataframe().to_csv(r"C.csv")