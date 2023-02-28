---
title: Release 1.3
date: 2019-03-29 08:00
category: news
authors: wradlib
tags: releases, github, python3
---

# Release 1.3

We have now released version 1.3 of wradlib.

This version contains more improvements and enhancements than bugfixes.

Now, these are the most important changes:

- **Python3 only**
With version 1.3 we dropped support for Python 2.7. The package is intensively tested with Python 3.6 and 3.7.

- **New CfRadial/ODIM_H5 reader based on xarray**
Contains functions to read and write CfRadial1 and upcoming CfRadial2 standard as well as ODIM_H5 standard radar data files. Makes intensive use of [xarray package](https://docs.xarray.dev/en/stable/), see also our [blog-post here](https://wradlib.org/2019/02/xarray_cfradial2_odimh5/). Examples are available in the [wradlib documentation](https://docs.wradlib.org/en/stable/notebooks/fileio/wradlib_xarray_radial_odim.html)

- **xarray powered plotting**
The plotting routines have been completely revised and build upon  {{wradlib}}  xarray DataArray Accessor. Helper functions for DataArray creation are implemented as well. [Extensive tutorials](https://docs.wradlib.org/en/stable/plotting.html) including map-making using cartopy are available too.

- **Revised Documentation**
The documentation structure has been reordered for better user experience.

For a complete list of changes refer to the [wradlib repository](https://github.com/wradlib/wradlib/commits/main).

As all new enhancements and additions might introduce regressions please report any issues you experience. Bugfix releases will be rolled out shortly. We kept our commitment to semver to stay backwards compatible regarding current workflows. One thing though is abandoning Python 2.7 where we are in line with many major python packages (eg. matplotlib).