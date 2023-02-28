---
title: Release 0.9.0
date: 2016-08-31 13:00
category: news
authors: wradlib
tags: releases, github, python2, python3
---

# Release 0.9.0

With this post, we announce the release of  {{wradlib}}  0.9.0. It finalizes our transition 
from example Python scripts to jupyter notebooks (as already announced in a 
[previous post](http://wradlib.org/2016/04/introducing-wradlib-jupyter-notebooks/)). As a result, 
the documentation pages have become more consistent, and the handling of examples and tutorials 
more convenient and interactive. We hope you'll agree!

## Interactive examples with jupyter notebooks 

As a consequence, the previous doc sections "Tutorials" and "Recipes" have been replaced by one single 
section [Tutorials and Examples](http://docs.wradlib.org/en/latest/notebooks.html).
The pages in that section were automatically built from jupyter 
(IPython) notebooks. These notebooks are distributed with the [new release](https://pypi.python.org/pypi/wradlib), 
and you can use them to interactively browse through our tutorials and examples. You can always download the latest notebooks 
from the [wradlib repository](https://github.com/wradlib/wradlib/tree/main/notebooks).

For those who do not know, yet, how to handle jupyter notebooks, we prepared a 
[quick tutorial](http://docs.wradlib.org/en/latest/jupyter.html). We also added a
brief (and certainly incomplete) [intro to Python](http://docs.wradlib.org/en/latest/notebooks/learnpython.html)
for those who would like to have some entry point to that language. This intro will certainly be further developed 
in the future.

In case you don't want to use notebooks: straight Python scripts are distributed alongside the notebooks with [each new release >= 0.9.0](https://pypi.python.org/pypi/wradlib).

## Get the example data from the new  {{wradlib}}  data repository 

We moved all the example data from the main
[wradlib repository](https://github.com/wradlib/wradlib/) to a new [data repository](https://github.com/wradlib/wradlib-data).
In order to run the notebooks on your computer, you need to download the example data archive yourself, and extract it to any directory on your computer. Then you need to create an environment variable pointing to that directory. After that, the example notebooks will automagically pull the required example data from that directory. See [here](http://docs.wradlib.org/en/latest/jupyter.html#how-can-i-get-the-example-data) for more detailed guidance on the process.

## Further changes in  {{wradlib}}  0.9.0 

Along with  {{wradlib}}  0.9.0, we also released a couple of minor, though hopefully useful new features and fixes, e.g.:

- `wradlib.io.read_RADOLAN_composite` can now read the new radolan [FZ product](https://github.com/wradlib/wradlib/pull/73),
- `wradlib.io.readDX` can now read gzipped DX data,
- `wradlib.io.read_Rainbow` was enhanced to read product pixmap data from rainbow5 files,
- fixed [incompatibility issue with scipy 0.18.0](https://github.com/wradlib/wradlib/issues/86),
- and fixed some other issues.

For more details on the new release, please visit our [release notes](http://wradlib.org/wradlib-docs/0.9.0/).

## Updating to  {{wradlib}}  0.9.0

Do you want to safely check out the new version and still keep the old one? Then you can install wraldib 0.9.0 into a new conda environment, e.g. like this: 

```shell

$ conda config --add channels conda-forge
$ conda create --name wradlib090 python=2.7
$ activate wradlib090
$ conda install wradlib

```

You can drop the first line if you already added the conda-forge channel.

For more details, or if you do not use Anaconda or conda, see our
[installation instructions](http://docs.wradlib.org/en/latest/gettingstarted.html).

In case you lost track of your Anaconda environments, you can use

```shell

$ conda --info envs

```

in order to get an overview. You can list all the packages (and their versions) in an environment (let's say wradlib090) via

```shell

$ conda list --name wradlib090

```

## For developers

Untagged MICRO-releases (0.9.1 and so on) are now released on [testpypi](https://testpypi.python.org/pypi/wradlib/). In the future, we hope to adopt this for [conda-forge](https://anaconda.org/conda-forge/wradlib), too. This might be interesting for users, too, for early checking of bug fixes (in case they do not want to use the bleeding edge code). 
