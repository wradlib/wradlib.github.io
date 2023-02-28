---
title: Utilizing xarray for CfRadial - ODIM_H5 interoperability
date: 2019-02-15 11:00
category: news
authors: wradlib
tags: cfradial2, odim, python
---

# Utilizing xarray for CfRadial - ODIM_H5 interoperability

We have just added a new feature for CfRadial2 - ODIM_H5 interoperability to wradlib.

wradlib is now able to read data from netcdf-based CfRadial1, CfRadial2 and hdf5-based ODIM_H5 (and other hdf5-flavours (GAMIC)).

wradlib is able to write data to CfRadial2 and ODIM_H5 files. This reader implementation uses

- [netcdf4](http://unidata.github.io/netcdf4-python/)
- [h5py](https://www.h5py.org/) and
- [xarray](https://xarray.pydata.org/)

The data is claimed using netcdf4-Dataset in a diskless non-persistent mode:

        :::python
        ncf = nc.Dataset(filename, diskless=True, persist=False)

Further the different netcdf/hdf groups are accessed via xarray opendataset and the NetCDF4DataStore:

        :::python
        xr.open_dataset(xr.backends.NetCDF4DataStore(ncf), mask_and_scale=True)

For hdf5 data scaling/masking properties will be added to the datasets before decoding. For GAMIC compound data will be read via h5py.

The data structure holds one `root` xarray dataset which corresponds to the CfRadial2 root-group and one or many `sweep_X` xarray datasets, holding the sweep data. Since for data handling xarray is utilized all xarray features can be exploited, like **lazy-loading**, **pandas-like indexing** on N-dimensional data and vectorized mathematical operations across multiple dimensions.

Using [cartopy](https://scitools.org.uk/cartopy/) and/or [dask](http://docs.dask.org/) the possibilities seem endless.

The writer implementation uses xarray for CfRadial2 output and relies on h5py for the ODIM_H5 output.

One word of warning, this implementation is considered experimental. Changes in the API should be expected.

We welcome everybody to check it out and report back any bugs, feature requests or other comments.
