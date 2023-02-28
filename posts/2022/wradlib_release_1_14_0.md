---
title: Release 1.14
date: 2022-03-18 14:00
category: news
authors: wradlib
tags: releases, github, python3
---

# Release 1.14

We have now released version 1.14 of wradlib.

Now, these are the most important changes:

**New features**

* zonalstats enhancements, new VectorSource class, geopandas connector and more
  For an example have a look here in the [docs](https://docs.wradlib.org/en/1.14.0/notebooks/zonalstats/wradlib_zonalstats_quickstart.html)

**Maintenance - Code**

* refactor deprecated xarray functionality
* use f-strings where appropriate
* remove unnecessary object-inheritance
* replace distutils.version.LooseVersion with packaging.version.Version
* use dict-literals

**Maintenance - Build/CI**

* cancel previous CV builds
* use provision-with-micromamba action

**Bugfixes**

* remove zero padding of bits in rainbow format (truncate excess bits from flagmap)
* raise ValueError if projection cannot be determined from source dataset
* output full timeslice when calling to_netcdf with no timestep 
* handle variable number of gates in CfRadial1 backend 
* use radar site altitude in bin_altitude calculation 
* take precision into account for RADOLAN WN product
* correct elevation for negative angles in iris/sigmet RAW data 
* fix AttributeError: 'str' object has no attribute 'item' 
* use start date/time if end date/time is missing for ODIM reader 

**New Contributors**
* [@binomaiheu](https://github.com/binomaiheu) made their first contribution in [#550](https://github.com/wradlib/wradlib/pull/550)

We like to thank all our contributors and all community members who ask questions and provide feedback on the various channels. Your contributions are very much appreciated. 

For a complete list of changes refer to the full **Changelog** [1.13.0...1.14.0](https://github.com/wradlib/wradlib/compare/1.13.0...1.14.0) or the [release notes](https://docs.wradlib.org/en/1.14.0/release_notes.html).

As all new enhancements and additions might introduce regressions, please report any issues you experience.
