---
title: Release 1.0.0
date: 2018-04-01 07:00
category: news
authors: wradlib
tags: releases, github, python2, python3
---

# Release 1.0.0

We have now released version 1.0.0 of wradlib. 

As some of you might be aware, version 1.x is generally considered as a major milestone, indicating that the software has all major features, and is considered reliable enough for general release.

The first commit to wradlib is now almost seven years ago. During these years, a lot of changes have been introduced in terms of algorithms, but also in terms of documentation and maintenance workflows. Yet, the API has become more and more stable, so we decided that wradlib is now mature enough for switching to a 1.x development line.

At the same time, we wanted to use that opportunity to address a couple of issues that we considered important from a developer's perspective. Addressing those issues will most likely break existing code and workflows. Yet, *this* is the time to do it, and doing it is vital to guarantee sustainable, efficient and reliable code development in the future. We cordially invite you to come along with us, and make use of version 1.0.0, even if it means that you might have to refactor your code. If you want to benefit from future improvements, this is the way to go! Limited resources will not allow us to further support the 0.x development line - from today on, it'll be legacy.

So, these are the most important changes:

# Removing redundant and outdated code
A lot of functions had been accumulating over time which remained immature, redundant, or scarcely used. Those functions and (partly) modules have been entirely removed. If you **really** miss one of them, [raise an issue](https://github.com/wradlib/wradlib/issues).   

# Conform with PEP conventions
Lots of function, class and variable names have been renamed in order to conform with [PEP conventions](https://www.python.org/dev/peps/pep-0008/#naming-conventions). It might hurt, first, but we are confident that refactoring will be quick.

# Revise georeferencing
Georeferencing has become more precise and transparent, making more use of gdal's potential. You will most likely not feel the difference - but we like it!

# Revise repository structure and CI workflows
In order to make developing and releasing more efficient, we fundamentally revised the repository structure: 
- the actual wradlib code remains under [http://github.com/wradlib/wradlib](http://github.com/wradlib/wradlib)
- the notebooks have been moved to [https://github.com/wradlib/wradlib-notebooks](https://github.com/wradlib/wradlib-notebooks)

# Documentation pages
The doc pages will mostly look the same, but they are now available under [http://docs.wradlib.org](http://docs.wradlib.org).

# For all developers
The pre-1.0 repository state is kept under [https://github.com/wradlib/wradlib-old](https://github.com/wradlib/wradlib-old) (not recommended). If you want to keep up with the latest developments, just stick with https://github.com/wradlib/wradlib. There's a small catch, though: if you want to base your development on the new wradlib/main, you need to merge it with brute force. On the local version of your current fork, you need to

```
$ git remote add upstream https://github.com/wradlib/wradlib.git
$ git checkout main
$ git fetch upstream
$ git reset --hard upstream/main
$ git push origin main --force
```