---
title: Release 1.2
date: 2018-10-31 08:00
category: news
authors: wradlib
tags: releases, github, python2, python3
---

# Release 1.2

We have now released version 1.2 of wradlib.

This version contains many bugfixes as well as improvements and enhancements. Most additions were pulled in within [Hacktoberfest](https://hacktoberfest.digitalocean.com/), the month-long celebration of open source software. Although this years Hacktoberfest is over, we encourage every wradlib user to join the party and envision the Hacktoberfest's 3 main mottos:

- ***Everyone is welcome!***
- ***Quantity is fun, Quality is key***
- ***Short term action, long term impact***

wradlib is building upon your support as users, feature requesters, bug reporters, collaborators and contributors. Thank you all, you're more than welcome.

Now, these are the most important changes:

- **New `classify`-module**
Contains Hydrometeorclassification (HMC) using 2D membershipfunctions. For incorporation of temperature data to HMC `get_radiosonde` function was added to `io.misc`. An example notebook covering the HMC workflow was added [to the documentation](https://docs.wradlib.org/en/1.2.0/notebooks/classify/wradlib_2d_hmc.html) (wradlib-notebooks). Other classification functions (clutter etc.) will be moved from `clutter`-module to `classify` in the next major version 2.0.

- **Speed-up interpolation functions**
By using special keyword argument `balanced_tree = False` for SciPy's `cKDTree` implementation the ipol-functions could be accelerated quite substantially (factor 100).

- **Introduced new header tokens for RADOLAN products**
German weather service (DWD) introduced new products using new header tokens (`VR`, `U`). The reader functions were enabled to work with these new products.

- **Revised documentation structure and CI workflows**
The documentation has been revised in terms of conformance and consistency, links were updated, typos fixed and CI workflow improved.

For a complete list of changes refer to the [wradlib repository](https://github.com/wradlib/wradlib/commits/main).