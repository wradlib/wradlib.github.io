---
title: Release 1.9
date: 2020-11-26 10:00
category: news
authors: wradlib
tags: releases, github, python3
---

# Release 1.9

We have now released version 1.9 of wradlib.

This version contains several bugfixes and some enhancements. For our Continuous Integration we've moved to `micromamba` which speeds up creation of Python environments.

Now, these are the most important changes:

**New features**

- make wradlib.io capable of consuming file-like objects
- read truncated RADOLAN composites

**Maintenance**

- use micromamba on CI to save CI time
- add Python 3.9 builds to all CI

**Bugfixes**

- add capability to decode old DX header 
- simplify dimension angle handling ODIM/GAMIC
- adapt to new string handling in h5py >= 3.0

We like to thank all our contributors and all community members who ask questions and provide feedback on the various channels. Your contributions are very much appreciated. 

For a complete list of changes refer to the [wradlib repository](https://github.com/wradlib/wradlib/commits/main).

As all new enhancements and additions might introduce regressions, please report any issues you experience.