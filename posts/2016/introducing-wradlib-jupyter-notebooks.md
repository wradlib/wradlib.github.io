---
title: introducing  {{wradlib}}  jupyter notebooks
date: 2016-04-26 11:00
category: wradlib
authors: wradlib
tags: wradlib, jupyter, notebook, documentation
---

# introducing  {{wradlib}}  jupyter notebooks

At a  {{wradlib}}  code-sprint early April, we thought about ways to make  {{wradlib}}  examples and tutorials more user-friendly, interactive and consistent.

Therefore, we decided to harmonise online tutorials and recipes together with the examples from the source distribution. All of them will be transformed as ready-to-use [jupyter](http://jupyter.org/) notebooks. These notebooks will be distributed along with wradlib, but they will also be rendered as tutorials/examples in the online documentation. In this ongoing process, all examples and tutorials will be reviewed and restructured if needed.

As a result, **wradlib users** will be able to walk through the examples interactively by using [jupyter](http://jupyter.org/) together with [IPython](https://ipython.org/). Interactively means that users can manipulate code and parameters on the fly and immediately evaluate the result. This is perfect for courses, lectures or tutorials. It will help users to better understand  {{wradlib}}  (as compared to just executing a script).

Still, for users who just want to run examples as plain Python scripts, we will also include these in the source distribution. Finally, all notebooks will be rendered for the online documentation.

For getting an idea about jupyter notebooks within  {{wradlib}}  have a look at these three (rendered) notebooks:

- [RADOLAN - Radar Products from German Weather Service](http://docs.wradlib.org/en/latest/notebooks/radolan.html),
- [Beam Blockage Calculation using DEM](http://docs.wradlib.org/en/latest/notebooks/beamblockage/wradlib_beamblock.html) and
- [Plot Additional Data](http://docs.wradlib.org/en/latest/notebooks/visualisation/wradlib_overlay.html)

We are currently in the process of transition. Successively, we will migrate all tutorials and examples.

Along the way, we decided to host our example datasets in the dedicated repository [wradlib-data](https://github.com/wradlib/wradlib-data). This way, we remove the "data overhead" from the source distribution. In order to run the examples locally, users need to carry out two steps:

 1. download the data to a local directory, and
 2. point to this directory by creating an environment variable `WRADLIB_DATA`.

The example data is automagically pulled from this location and used in the examples and notebooks. Detailed instructions will be included in the documentation.

From a **wradlib developers'** perspective, the advantages of the new approach are huge, too:

> We only write a notebook **once**.

This notebook will serve as both as test code and user example, and it will automatically be rendered for online documentation. This way, all code examples will be consistent and in sync.

The new  {{wradlib}}  notebook workflow in more detail:

- document code example or tutorial only once as jupyter notebook
- convert notebooks for  {{wradlib}}  tests in CI ([convert_notebooks.sh](https://github.com/wradlib/wradlib/blob/main/scripts/convert_notebooks.sh))
- render notebooks for  {{wradlib}}  docs in CI ([render_notebooks.sh](https://github.com/wradlib/wradlib/blob/main/scripts/render_notebooks.sh),
  [nbsphinx](https://github.com/spatialaudio/nbsphinx))

If you have ideas and suggestions about extending the tutorials, notebooks or recipe sections, take your chance and contact us.










