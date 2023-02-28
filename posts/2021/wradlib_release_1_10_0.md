---
title: Release 1.10
date: 2021-06-01 13:00
category: news
authors: wradlib
tags: releases, github, python3
---

# Release 1.10

We have now released version 1.10 of wradlib.

This version contains several enhancements and some bugfixes. For our Continuous Integration we've moved to GitHub Actions for all of our production repositories.

Now, these are the most important changes:

**New features**

- add [ODIM/GAMIC/CfRadial/RADOLAN backends](https://docs.wradlib.org/en/latest/notebooks/fileio/wradlib_xarray_backends.html) for reading radar data into xarray Datasets
- decode IRIS DB_XHDR as numpy structured array

**Maintenance**

- use GitHub Actions as CI
- use new ``xarray.BackendEntryPoint``
- address several DeprecationWarnings (eg. numpy)
- create/use earthdata credentials for srtm data (users would need to do so, if the want to use srtm data)

**Bugfixes**

- fix _FillValue and GAMIC dynamic range 
- fix doctest example in vpr-module
- fix handle kwarg change scipy.cKDTree

We like to thank all our contributors and all community members who ask questions and provide feedback on the various channels. Your contributions are very much appreciated. 

For a complete list of changes refer to the [wradlib repository](https://github.com/wradlib/wradlib/commits/main).

As all new enhancements and additions might introduce regressions, please report any issues you experience.