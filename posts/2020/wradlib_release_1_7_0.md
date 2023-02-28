---
title: Release 1.7
date: 2020-06-12 08:00
category: news
authors: wradlib
tags: releases, github, python3
---

# Release 1.7

We have now released version 1.7 of wradlib.

This version contains several bugfixes and enhancements.

Now, these are the most important changes:

- **Improvements in georef.projection module**
    
    Edouard Goudenhoofdt (RMI - Belgium) enhanced the projection-module with new functions to create radar centric and default earth projections.

- **Implementation of interpolation functions working on regular grids**

    In another example of joining forces of Edouard Goudenhoofdt (RMI - Belgium) and Kai Mühlbauer (University Bonn - Germany) new interpolators working on regular grids have been implemented.
    This will be the first serve of a general overhaul of the interpolation classes. 
    
- **Rework of PhiDP/KDP algorithm (Vulpiani et.al.)**
    
    Kai Mühlbauer (University Bonn - Germany) added a new generalized `derive` function for calculation of derivation which significantly improves NaN-handling and speed. All other parts of the Vulpiani algorithm have been revised in terms of speed, handling of ND-arrays and parametrization.
    
- **Implement decoding of DB_RAINRATE2 in IRIS/Sigmet reader**

    Alper Çubuk (TSMS - Turkey) added decoding of RAINRATE2  

- **Bugfixes**
    
    The wradlib community found several bugs which are now fixed.   

We like to thank all our contributors and all community members who ask questions and provide feedback on the various channels. Your contributions are very much appreciated. 

For a complete list of changes refer to the [wradlib repository](https://github.com/wradlib/wradlib/commits/main).

As all new enhancements and additions might introduce regressions please report any issues you experience.