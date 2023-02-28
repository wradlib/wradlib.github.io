---
title: Simple Treeview with traits
date: 2016-03-11 10:00
category: prog
authors: kmuehlbauer
tags: rainbow5, treeview, python
---

# Simple Treeview with traits

Since we are continuously receiving inquiries regarding the work with Rainbow5(TM) radar data, I will present here a nice way of visualizing the dictionary representation of an arbitrary Rainbow5 file.

This code snippet makes use of the python packages traits and traitsui.

Installing traits is as easy as:

    :::bash
    $ pip install traitsui

By adapting this gist a treeview representation of the loaded dictionary is given in a simple qt-gui:

<script src="https://gist.github.com/wradlib/9037b8a67dfbcff3b7de.js"></script>

Now you can browse the contents of your versatile Rainbow5 data file and examine the needed dictionary-keys to fit in your data loading routine.

![Example view](simple-treeview-with-traits.png)

Credits: [Thorsten Kranz](http://stackoverflow.com/users/1156006/thorsten-kranz) [View at StackOverflow](http://stackoverflow.com/questions/15023333/simple-tool-library-to-visualize-huge-python-dict)

