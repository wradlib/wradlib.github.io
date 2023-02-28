---
title: easy install using conda-forge
date: 2016-03-17 15:00
category: wradlib
authors: wradlib
tags: conda, windows, osx, linux, python
---
# easy install using conda-forge

With the help of an outstanding community effort named [conda-forge](https://conda-forge.github.io/),
wradlib can now be more conveniently installed on _**linux**_, _**windows**_ and _**osx**_.

Until now, installing wradlib and its dependencies could be tricky, with each OS having its own issues. On Windows, we so far recommended
to satisfy all depencies via [Python(x,y)](https://python-xy.github.io/). This was convenient; however, it limited users to Python 2.7,
and, more importantly, to 32-bit Python. This was a serious drawback particularly for memory-intensive applications.

With this post, we present a new installation approach that is harmonised across platforms. Using
[conda-forge/wradlib-feedstock](https://github.com/conda-forge/wradlib-feedstock), we provide installable wradlib packages
for all major OS (accounting for different python and numpy versions, and offering 32-bit builts for Windows, if desired).
All builts are tested and uploaded to the [conda-forge channel](https://anaconda.org/conda-forge/wradlib).

The default-conda channel provides many wradlib dependencies out of the box, but not all.
Hence, we also contributed to the [conda-forge/gdal-feedstock](https://github.com/conda-forge/gdal-feedstock)
making it the first feedstock serving two different package versions (gdal 1.11.4 and 2.0.2).

As a result, wradlib can now be conveniently installed using the [conda package manager](http://conda.pydata.org/docs/intro.html).
Windows users should be aware, though, that this approach is **not** compatible with Python(x,y). So you need to make a decision.

So this is the basic walk through:

1. Install the [Anaconda environment of your choice](https://www.continuum.io/downloads)

2. Clone the root environment or create one from scratch

        :::bash
        $ conda create --name wradlib --clone root
        or
        $ conda create --name wradlib python=2.7

3. Add the conda-forge channel

        :::bash
        $ conda config --add channels conda-forge

4. Activate wradlib environment

    * Linux

            :::bash
            $ source activate wradlib

    * Windows

            :::bash
            > activate wradlib

5. Install wradlib (and dependencies)

        :::bash
        (wradlib) $ conda install wradlib

6. Set GDAL_DATA environment variable (needed for georeferencing)

    * Linux/OSX bash

            :::bash
            (wradlib) $ export GDAL_DATA=/path/to/anaconda/envs/wradlib/share/gdal

    * Windows CMD.exe

            :::bash
            [wradlib] > setx GDAL_DATA C:\path\to\anaconda\envs\wradlib\Library\share\gdal

7. Optional dependencies can be installed OS independent with `pip`

        :::bash
        (wradlib) $ pip install xmltodict

* * *

We hope that this new approach will make the installation of wradlib more convenient, and, as a result, enhance its usability
on all major platforms - thanks to [Anaconda](https://www.continuum.io/why-anaconda) from Continuum(R) and the conda-forge
community effort.





