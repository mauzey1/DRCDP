import cmor
import xarray as xr
import xcdat as xc
import numpy as np
import json
import sys,os


cmorTable = '../Tables/obs4MIPs_Aday.json' ; # Aday,Amon,Lmon,Omon,SImon,fx,monNobs,monStderr - Load target table, axis info (coordinates, grid*) and CVs
inputJson = 'DRCDP_demo_input.json' ; # Update contents of this file to set your global_attributes
inputFilePath = 'DRCDP_demo_data.nc'
inputVarName = 'tasmax'
outputVarName = 'tasmax'
outputUnits = 'K'

# Open and read input netcdf file, get coordinates and add bounds
f = xc.open_dataset(inputFilePath,decode_times=False)
d = f[inputVarName]
lat = f.lat.values 
lon = f.lon.values 
time = f.time.values  
f = f.bounds.add_missing_bounds(axes=['X', 'Y'])
f = f.bounds.add_bounds("T")
tbds = f.time_bnds.values
d = np.where(np.isnan(d),1.e20,d)

# Initialize and run CMOR. For more information see https://cmor.llnl.gov/mydoc_cmor3_api/
cmor.setup(inpath='./',netcdf_file_action=cmor.CMOR_REPLACE_4) #,logfile='cmorLog.txt')
cmor.dataset_json(inputJson)
cmor.load_table(cmorTable)

# Create CMOR axes
cmorLat = cmor.axis("latitude", coord_vals=lat[:], cell_bounds=f.lat_bnds.values, units="degrees_north")
cmorLon = cmor.axis("longitude", coord_vals=lon[:], cell_bounds=f.lon_bnds.values, units="degrees_east")
cmorTime = cmor.axis("time", coord_vals=time[:], cell_bounds=tbds, units= f.time.units)
cmoraxes = [cmorTime,cmorLat, cmorLon]

# Setup units and create variable to write using cmor - see https://cmor.llnl.gov/mydoc_cmor3_api/#cmor_set_variable_attribute
varid   = cmor.variable(outputVarName,outputUnits,cmoraxes,missing_value=1.e20)
values  = np.array(d,np.float32)[:]

# Append valid_min and valid_max to variable before writing using cmor - see https://cmor.llnl.gov/mydoc_cmor3_api/#cmor_set_variable_attribute
cmor.set_variable_attribute(varid,'valid_min','f',2.0)
cmor.set_variable_attribute(varid,'valid_max','f',3.0)
# 
# Prepare variable for writing, then write and close file - see https://cmor.llnl.gov/mydoc_cmor3_api/#cmor_set_variable_attribute
cmor.set_deflate(varid,1,1,1) ; # shuffle=1,deflate=1,deflate_level=1 - Deflate options compress file data
cmor.write(varid,d,len(time)) 
cmor.close()
f.close()
