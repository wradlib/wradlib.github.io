---
title: Release 1.13
date: 2021-11-14 11:00
category: news
authors: wradlib
tags: releases, github, python3
---

# Release 1.13

We have now released version 1.13 of wradlib.

After missing `requirements_optional.txt` in the source distribution which has been uploaded to ``PyPI`` as `1.12.0`, we had to remove this version from ``PyPI`` again. The problem was that the installation from the source distribution was not possible without this file. 

Anyway, this was fixed and wradlib `1.13.0` was released shortly after. This version contains two enhancements and a whole bunch of bugfixes. Some dependencies have been made optional as well. The hard dependencies of wradlib are codewise: 

- deprecation
- matplotlib
- numpy
- scipy
- xarray>=0.17.0  

This has no affect on current versions `< 2.0` doing normal install or by installing via conda-forge. But you can already test this by installing wradlib using pip:

    :::bash
    $ python -m pip install wradlib==1.13.0 --no-deps

Or from inside the latest cloned/extracted wradlib github-main:

    :::bash
    $ python -m pip install . --no-deps

Now, these are the most important changes:

**New features**

- add [IRIS/sigmet backend](https://docs.wradlib.org/en/1.13.0/notebooks/fileio/wradlib_iris_backend.html) for reading radar data into xarray Datasets
- add [Rainbow5 backend](https://docs.wradlib.org/en/1.13.0/notebooks/fileio/wradlib_rainbow_backend.html) for reading radar data into xarray Datasets

**Maintenance**

- optionalize dependencies (dask, gdal, h5netcdf, h5py, netCDF4, requests, xmltodict)
- use pytest-doctestplus to handle optional dependencies in doctests
- fix docstrings

**Bugfixes**

- use reasonable default values in io.xarray.to_odim (gain, offset, nodata, undetect, fillvalue)
- add cf attributes when reading GAMIC files
- fix regression in legacy GAMIC reader
- catch dt.accessor TypeError
- fix thread-lock issue, if dask is not installed
- use int instead np.int in radolan header parser
- fix several tests

We like to thank all our contributors and all community members who ask questions and provide feedback on the various channels. Your contributions are very much appreciated. 

For a complete list of changes refer to the full **Changelog** [1.11.0...1.13.0](https://github.com/wradlib/wradlib/compare/1.11.0...1.13.0) or the [release notes](https://docs.wradlib.org/en/1.13.0/release_notes.html).

As all new enhancements and additions might introduce regressions, please report any issues you experience.
