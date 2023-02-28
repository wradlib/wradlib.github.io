---
title: Release 1.4
date: 2019-05-24 14:00
category: news
authors: wradlib
tags: releases, github, python3
---

# Release 1.4

We have now released version 1.4 of wradlib.

This version contains several bugfixes and three enhancements.

Now, these are the most important changes:

- **enhance/rewrite fuzzy echo classifier**
Aart Overeem (KNMI) not only spotted a long existing bug in `dp.texture` but also extended the `clutter.classify_echo_fuzzy` using DR (depolarization ratio, new function `dp.depolarization`) and CPA (clutter phase alignment). 

- **read sigmet/iris ingest files, redesign reader**
This addition was suggested by Alex Schueth (Texas Tech Univ.). He provided ingest data files and tested the implementation. Feedback from Canberk Karadavut and Alper Çubuk (TSMS) was incorporated into the redesign of the reader.  

- **parametrized ODIM_H5 reader based on xarray**
This was suggested by Edouard Goudenhoofdt (RMI) to speed up loading time of ODIM_H5 data files. He provided initial implementation, which led to a minor re-write of the reader. Finally the implementation is flexible and powerful at the same time. The user can decide by keywords, which and how the data should be read. He also added a neat function to profile  {{wradlib}}  tests.

- **Bugfixes**
Paul Pazdersik suggested the removal of an unnecessary `seek` in radolan-reader. Canberk Karadavut and Alper Çubuk found a problem in decoding of `DB_FLIQUID2` in sigmet/iris-reader and added a fix. Bahtiyor Zohidov spotted a problem with the 2D HMC non-precip handling and helped with fixing. Sebastian Ernst and Zach Sherman helped to keep  {{wradlib}}  future-proof.  

We like to thank all our contributors and all community members who ask questions and provide feedback on the various channels. Your contributions very much appreciated. 

For a complete list of changes refer to the [wradlib repository](https://github.com/wradlib/wradlib/commits/main).

As all new enhancements and additions might introduce regressions please report any issues you experience.