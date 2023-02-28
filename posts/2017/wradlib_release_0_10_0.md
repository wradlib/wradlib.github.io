---
title: Release 0.10.0
date: 2017-04-10 16:00
category: news
authors: wradlib
tags: releases, github, python2, python3
---

# Release 0.10.0

We are happy to announce the release of wradlib 0.10.0.

## Highlights

Highlight of this release is the implementation of matching of GPM/TRMM-platforms
with ground radar observations in 3D. A step-by-step guide is available as
[jupyter notebook](http://wradlib.org/wradlib-docs/0.10.0/notebooks/match3d/wradlib_match_workflow.html). Also the wradlib raster handling
has been improved considerably with [PR#137](https://github.com/wradlib/wradlib/pull/137).

## Further changes in wradlib 0.10.0

There are also a couple of community enhancements and other improvements and fixes.

Community Contribution by [Christian Chwala](https://github.com/cchwala):

- `wradlib.io.read_RADOLAN_composite` accept file handles [PR#114](https://github.com/wradlib/wradlib/pull/114),
- `wradlib.io.read_Rainbow` accept file handles [PR#140](https://github.com/wradlib/wradlib/pull/140).

Community Contribution by [franklinvv](https://github.com/franklinvv):

- `wradlib.georef.get_radolan_grid` was enhanced to read extended-RADOLAN-grid [PR#119](https://github.com/wradlib/wradlib/pull/119).

Improvements:

- Merged the curvelinear grid plotting functions into the normal plotting functions. Added **contour** and **filled contour** plotting capabilities.
- Generic netcdf reader can read **groups** now.
- Added `wradlib.qual.cum_beam_block_frac` to compute cumulative beam blockage.
- Added **Earth Curvature Display** to [beam blockage notebook](http://wradlib.org/wradlib-docs/0.10.0/notebooks/beamblockage/wradlib_beamblock.html)
- Enhance `wradlib.georef.read_gdal_values` to read multiband data.

Fixes:

- The build process on Travis-CI was significantly improved by running test-suites in dedicated threads/subprocesses.
- We also fixed some documentation inconsistencies.
- Several bugs were fixed in `wradlib.qual.pulse_volume`, `wradlib.georef.transform_geometry`, `wradlib.util.find_bbox_indices` and `wradlib.ipol.cart2irregular_spline`.
- Several other minor fixes.

For more details on the new release, please visit our [release notes](http://wradlib.org/wradlib-docs/0.10.0/release_notes.html).
