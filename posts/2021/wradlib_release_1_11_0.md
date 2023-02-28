---
title: Release 1.11
date: 2021-09-02 13:00
category: news
authors: wradlib
tags: releases, github, python3
---

# Release 1.11

We have now released version 1.11 of wradlib.

This version contains two enhancements and a whole bunch of bugfixes. We changed our branch naming to `main`. 

Now, these are the most important changes:

**New features**

- add support for RADOLAN HG product
- add %M, %J and %Y RADOLAN products

**Maintenance**

- rename master -> main
- fix docstrings (links, types, minor issues)

**Bugfixes**

- minor fixes in GAMIC and CfRadial readers
- use default values for ODIM/OPERA what-group
- do not restrict variables, but read all variables for Cf/Radial1 data
- correct calculation of angle resolution in ODIM/GAMIC xarray readers
- add mode-kwarg to radolan coordinates/grid functions
- add kwarg origin and FutureWarning to IRIS CartesianImage reader
- remove unnecessary gridshape kwarg from docstring in CartesianVolume
- correctly handle single/multiple elevations in wradlib.vis.plot_scan_strategy
- fix ODIM xarray reader issues
- mention dask in all open_*_mfdataset functions

We like to thank all our contributors and all community members who ask questions and provide feedback on the various channels. Your contributions are very much appreciated. 

For a complete list of changes refer to the [wradlib repository](https://github.com/wradlib/wradlib/commits/main) or the [release notes](https://docs.wradlib.org/en/1.11.0/release_notes.html).

As all new enhancements and additions might introduce regressions, please report any issues you experience.