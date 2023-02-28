---
title: Release 1.5
date: 2019-08-02 14:00
category: news
authors: wradlib
tags: releases, github, python3
---

# Release 1.5

We have now released version 1.5 of wradlib.

This version contains several bugfixes and enhancements.

Now, these are the most important changes:

- **further consolidation of xarray based ODIM_H5 and Cf/Radial readers/writers**

    We have added [examples](https://docs.wradlib.org/en/1.5.0/notebooks/fileio/wradlib_xarray_radial_odim.html) of how to read/write these files and also a [real-live example](https://docs.wradlib.org/en/1.5.0/notebooks/fileio/wradlib_load_DWD_opendata_volumes.html) using data from German Weather Service.
    In this example we show how our implementation combines all 20 files (two moments, 10 sweeps) into one xarray powered structure, which can be exported to single CfRadial2 or ODIM_H5 volume files.
    For exploitung `dask` for lazy/parallelized processing the `chunk` keyword can be used to transparently use dask with xarray.
    
    We encourage all users to dive into Xarray based processing as wradlib will continuously update it's codebase utilizing Xarray based processing.

- **xarray wrapper for RADOLAN data**
    
    As a first attempt we added `loaddata='xarray'` keyword argument to the `read_radolan_composit` function. This will output the data wrapped in an Xarray Dataset with attached coordinates of the radolan stereographic projection. A short example can be found [here](https://docs.wradlib.org/en/1.5.0/notebooks/radolan/radolan_quickstart.html#RADOLAN-Xarray-reader).

- **speedup zonal statistics**
    
    Using GDAL powered `/vsimem` (a virtual memory driver) and by creation of spatial and attribute index files as well as by combining attribute and property reads, we could significantly improve performance. The CI time of the zonal stats example went down to 80 seconds from over 360 seconds.    

- **Bugfixes**
    
    The wradlib community found several bugs which are now fixed (multidimensional calling in `gradient_along_axis`, missing destination projection in destination dataset in `reproject_raster_dataset` and several more).   

We like to thank all our contributors and all community members who ask questions and provide feedback on the various channels. Your contributions very much appreciated. 

For a complete list of changes refer to the [wradlib repository](https://github.com/wradlib/wradlib/commits/main).

As all new enhancements and additions might introduce regressions please report any issues you experience.