---
title: Release 1.6
date: 2020-03-12 10:00
category: news
authors: wradlib
tags: releases, github, python3
---

# Release 1.6

We have now released version 1.6 of wradlib.

This version contains several bugfixes and enhancements.

Now, these are the most important changes:

- **Implementation of multi file ODIMH5 reader/writer**

    In a combined effort of Edouard Goudenhoofdt (RMI - Belgium) and Kai Mühlbauer (University Bonn - Germany) a new implementation of a multi-file ODIMH5-reader has been added.
        
    The main difference to the other implementation is the ability to handle a timeseries of ODIMH5 data.
    Another great advantage lies in the implementation itself, where retrieving of metadata is achieved by using `h5py`, `h5netcdf` or `netcdf` depending on the users needs, which accounts for speed. 
    The reading of datasets itself is decoupled from the metadata using xarray.
    
    Please find the implementation details included with a usage example in [this comprehensive notebook](https://docs.wradlib.org/en/1.6.0/notebooks/fileio/wradlib_odim_multi_file_dataset.html).  
    
- **Improvements in georef.raster module**
    
    Edouard Goudenhoofdt (RMI - Belgium) enhanced the raster-module with the ability to automatically retrieve and project SRTM elevation data.
    
- **Improve and simplify zr.module**
    
    Kai Mühlbauer (University Bonn - Germany) took the chance to strip the zr-module from old code and made the functions work with multidimensional input data.

- **Bugfixes**
    
    The  {{wradlib}}  community found several bugs which are now fixed.   

We like to thank all our contributors and all community members who ask questions and provide feedback on the various channels. Your contributions are very much appreciated. 

For a complete list of changes refer to the [wradlib repository](https://github.com/wradlib/wradlib/commits/main).

As all new enhancements and additions might introduce regressions please report any issues you experience.