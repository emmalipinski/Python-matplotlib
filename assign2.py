#!/usr/bin/env python3

#import packages

import matplotlib
import matplotlib.pyplot as plt
import sys
import statistics as stat
import numpy

#list of command line arguments. Last argument is output file
inFile = sys.argv[1:-1]
outFile = sys.argv[-1]

#load data
for i in inFile:
    with open(i) as f:
        header = f.readline().rstrip().split(',') #rstrip removes newline
        data = []
        for line in f:
            data.append(line.rstrip().split(','))
        for j in range(len(data)):
            data[j] = list(map(int, data[j]))

        #get values of cell counts
        values = [x[1:] for x in data]
        #find means and standard deviations
        means = list(map(stat.mean, values))
        stDev = list(map(numpy.std, values))
        #get time points
        x = [x[0] for x in data]
        #plot data with error bars for each dataset
        plt.errorbar(x,means,yerr=stDev, fmt='-o', label=header[0])

#labels and legend
plt.xlabel("Time (min)")
plt.ylabel("Cell Count")
plt.legend(loc = 'best')
#save figure
plt.savefig(outFile)












