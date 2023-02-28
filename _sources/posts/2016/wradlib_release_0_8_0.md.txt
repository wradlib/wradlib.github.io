---
title: Release 0.8.0
date: 2016-03-10 13:00
category: news
authors: wradlib
tags: releases, github, python2, python3
---

# Release 0.8.0

As already announced in previous articles ([#1](http://wradlib.org/2016/02/wradlib-at-github/), 
[#2](http://wradlib.org/2016/02/wradlib-python3-compatibility/)), we entirely moved our code development 
from [bitbucket](https://bitbucket.org/wradlib/wradlib) to [github](https://github.com/wradlib), 
and applied a major code revision to make  {{wradlib}}  compatible with both Python 2.7 and 3.5. The tremendous 
efforts to achieve this have been spearheaded by Kai Muehlbauer (University of Bonn). Thanks also to Jonathan J. Helmus from Argonne National Laboratory for valuable advice in the transition period. 

Please understand that the [bitbucket repository](https://bitbucket.org/wradlib/wradlib) will no longer be updated, and only hosted as legacy code.

wradlib 0.8.0 is the first release that follows upon this major transition. As a user, you should (hopefully) not feel much of a difference. The most obvious change is that you will now find the library documentation on [http://wradlib.org/wradlib-docs](http://wradlib.org/wradlib-docs). 
[http://wradlib.org](http://wradlib.org) itself will serve as a new central service to keep you updated on new developments. 

You can keep on installing new  {{wradlib}}  releases with the `pip install` mechanism. Cloning the bleeding edge code will require to install a `git` client and point it to [https://github.com/wradlib/wradlib](https://github.com/wradlib/wradlib). Developers are cordially invited to fork from that repository and share their developments via Pull Requests.

Apart from these changes,  {{wradlib}}  0.8.0 includes a couple of improvements particularly related to the 
[zonalstats module](http://docs.wradlib.org/en/latest/zonalstats.html). Please expect further changes to that module in the future, making it more generic and more convenient.

We are now using Travis CI to continuously scrutinize the integrity of our codebase. Still, the transition might imply a 
couple issues that we have not yet identified. Please bear with us, and do not hesitate to report issues [here](https://github.com/wradlib/wradlib/issues),
or to seek help in our [user forum](https://groups.google.com/forum/?fromgroups#!forum/wradlib-users).   
