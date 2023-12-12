# Python-matplotlib
Python assignment to learn the basics of matplotlib.

In this assignment you'll get more familiar with reading files and working with lists and learn the basics of matplotlib, a powerful and high-quality graphing library. The goal is to plot changes in cell counts over time under different conditions.

Import matplotlib like this:

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

This will prevent matplotlib from trying to open a display, which it does by default, even if you don't see it.

You will create a python script, assign2.py, that takes an arbitrary number of input arguments, and an output file (the last argument is the name of the output file). Make sure that each input file may have an arbitrary (but fixed) number of columns (representing different replicates of the same experiment).

The input file has a header that specifies the name of the data followed by rows of x,y data like this:
No drug
0,72,39,16,62
20,71,45,17,67
40,77,51,21,77
60,76,51,23,85
80,84,56,27,95
100,93,56,27,103
120,99,55,31,109
140,93,55,37,117
160,103,56,41,127

The first column of the data is the time points of the experiments. The other columns are cell counts.

Your script will plot the data using a line and circle style and save the result to the output file (out0.60.png in this example).
Add axis labels and a legend. The legend should be positioned in the "best" position as determined by matplotlib. The data is labeled according to the header value provided in the input file. You should plot the average (mean) of these values for each time point. In addition to plotting the mean, plot the standard deviation with errorbars.

./assign2.py  in.0 in.1 in.2 out0.90.png





