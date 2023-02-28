---
title: wradlib moves forward
date: 2023-02-10 20:00
category: news
authors: kmuehlbauer
tags: xradar, wradlib, news
---

#  {{wradlib}}  moves forward 

As you probably all know by now,  {{wradlib}}  is moving forward now and in the near future. There are several aspects which 
are laid out in this blog post.

## Xradar

In the upcoming version 1.19  {{wradlib}}  will use [xradar](https://docs.openradarscience.org/projects/xradar) for reading/writing 
radar data. For this to happen, I've ported all related code from  {{wradlib}}  to xradar. Xradar, a package dedicated to read 
and write radar data based on xarray structures, was launched in late August 2022, on initiative of Max Grover and me.

A compatibility layer is kept in  {{wradlib}}  which enables users to continue using their code and early adopt full xradar 
dependency.

##  {{wradlib}}  2.0

After the above switch to [xradar](https://docs.openradarscience.org/projects/xradar) in  {{wradlib}}  1.19 there will be quite 
some new code based on xarray data structures flowing into wradlib. We'll have to cut off some old braids, too. But, 
using the Scientific Python stack with all those great packages, like Xarray, Dask, matplotlib, Jupyter, NumPy, SciPy, 
to name only a few,  {{wradlib}}  is still standing on the shoulders of giants.

## wradlib-data

The [wradlib-data](https://github.com/wradlib/wradlib-data) repository is on the move to use pooch for retrieving datasets. 
That way you only have to install shallow package and the data will be fetched from the repo on demand. 

## wradlib-notebooks

The [wradlib-notebooks](https://github.com/wradlib/wradlib-notebooks) have been updated and restructured a bit to be in 
line with the latest developments. There is a bit of work ahead to get all notebooks up-to-date using recent technology.

## wradlib-docs

The split of  {{wradlib}}  into three repos back in early 2016 was no easy decision. It helped a lot in gaining as much 
as possible from the emerging [GitHub](https://github.com) cloud system. Now, as GitHub has tremendously advanced - huge
thanks to GitHub for providing this all for free for us open source projects - it has come the time to get the 
[wradlib-docs](https://github.com/wradlib/wradlib-docs) back into the  {{wradlib}}  main repository. We can much more easily 
keep everything together without any loose ends. This will most likely happen just after  {{wradlib}}  1.19 release. In the 
same time the docs will have a refresh as well. We will also see a new theme by then.
    
## wradlib-users forum

We've seen any kind of questions and help in our forum over the years. I always appreciated the constructive and friendly
discussions. Within the [openradar community](https://openradarscience.org/) we've discussed how to get more close 
together with respect to help users and discuss any matters of weather radar and more. Our not so new 
[openradar-discourse](https://openradar.discourse.group/) discussion-group is our new location where users, 
developers, scientists and other weather radar enthusiasts can come together. The wradlib-users forum will go out of 
service later this year. 

I hope to see you around - Stay well, Everyone!
