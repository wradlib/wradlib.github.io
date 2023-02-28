---
title: Release 1.8
date: 2020-09-03 11:00
category: news
authors: wradlib
tags: releases, github, python3
---

# Release 1.8

We have now released version 1.8 of wradlib.

This version contains several bugfixes and enhancements. We've also done a lot of maintenance with regard to Continuous Integration as well as handled upstream deprecations.

Now, these are the most important changes:

**New features**

- add WN product size (1200,1000) to radolan grid, add test for correct reference point (lower left)
- add `WN` and `YW` products to radolan to xarray converter
- add `wradlib.show_versions()` to easily get state of wradlib and it's dependencies (thanks to [xarray](http://xarray.pydata.org/en/stable/))  

**Maintenance**

- add azure CI tests
- code formatting according to black/isort/flake8, add setup.cfg
- add github templates
- remove deprecated and unused code and handle upstream deprecations
- use pytest for testing, implement "@require_data" to be able to run tests in case of missing wradlib-data 
- enhance azure ci workflow by adding flake8 linter and uploading coverage

**Bugfixes**

- fix srtm downloads windows path issues and region selection
- make `georeference_dataset` work with ND datasets
- update `vis.plot_scan_strategy()`
- add switch to keep elevation data unaltered (DWD terrain following scan)
- always translate ODIM attributes to CF attributes 
- specify keys (sweep_groups) which should be saved using to_netcdf 
- rework ODIM RHI elevation angle retrieval 

We like to thank all our contributors and all community members who ask questions and provide feedback on the various channels. Your contributions are very much appreciated. 

For a complete list of changes refer to the [wradlib repository](https://github.com/wradlib/wradlib/commits/main).

As all new enhancements and additions might introduce regressions, please report any issues you experience.