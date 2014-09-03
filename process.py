import sys
from windrose import WindroseAxes
from matplotlib import pyplot as plt
import matplotlib.cm as cm
from numpy.random import random
from numpy import arange
import os
import numpy as np


def plot(prefix, spds, dirs):
    ws = np.array(spds)
    wd = np.array(dirs)

    def new_axes():
        fig = plt.figure(figsize=(8, 8), dpi=80, facecolor='w', edgecolor='w')
        rect = [0.1, 0.1, 0.8, 0.8]
        ax = WindroseAxes(fig, rect, axisbg='w')
        fig.add_axes(ax)
        return ax, fig

    def set_legend(ax):
        l = ax.legend(axespad=-0.10, title="m/s", loc=0)
        plt.setp(l.get_texts(), fontsize=8)

    #windrose like a stacked histogram with normed (displayed in percent) results
    ax, fig = new_axes()
    ax.bar(wd, ws, normed=True, opening=0.8, edgecolor='white', bins=arange(0,max(ws),5))
    set_legend(ax)
    tokens = prefix.split("/")[-1].split("_")
    if tokens[0] == "Dust":
        title = "%s Dust" % tokens[1]
    else:
        title = tokens[0]
    
    plt.title(title, y=1.08)
    fig.savefig("%s-fig1.png" % prefix)

    #Another stacked histogram representation, not normed, with bins limits
    ax, fig = new_axes()
    ax.box(wd, ws, normed=True, bins=arange(0,max(ws),5))
    set_legend(ax)
    plt.title(title, y=1.08)
    fig.savefig("%s-fig2.png" % prefix)

    #A windrose in filled representation, with a controled colormap
    ax, fig = new_axes()
    ax.contourf(wd, ws, normed=True, bins=arange(0,max(ws),5), cmap=cm.hot)
    set_legend(ax)
    plt.title(title, y=1.08)
    fig.savefig("%s-fig3.png" % prefix)


    #Same as above, but with contours over each filled region...
    ax, fig = new_axes()
    ax.contourf(wd, ws, normed=True, bins=arange(0,max(ws),5), cmap=cm.hot)
    ax.contour(wd, ws, normed=True,bins=arange(0,max(ws),5), colors='black')
    set_legend(ax)
    plt.title(title, y=1.08)
    fig.savefig("%s-fig4.png" % prefix)

    #...or without filled regions
    ax, fig = new_axes()
    ax.contour(wd, ws, normed=True, bins=arange(0,max(ws),5), cmap=cm.hot, lw=3)
    set_legend(ax)
    plt.title(title, y=1.08)
    fig.savefig("%s-fig5.png" % prefix)

    ##print ax._info
    #plt.show()

def main(folder="data"):    
    for filename in filter(lambda x:x.endswith(".csv"), os.listdir(folder)):
        path = "%s/%s" % (folder, filename)
        plot_path = "%s/plots" % folder
        if not os.path.exists(plot_path):
            os.mkdir(plot_path)
        print path
        f = open(path)
        f.readline()
        directions = []
        speeds = []
        for line in f:
            cols = line.split(",")    
            direction = cols[5]
            speed = cols[6]
            try:
                direction = int(direction)
                speed = int(speed) * 0.44704
            except:
                continue

            directions.append(direction)
            speeds.append(speed)
            
        plot("%s/plots/%s" % (folder, filename.split(".")[0]), speeds, directions)
        
if __name__ == "__main__":
    main(sys.argv[1])

