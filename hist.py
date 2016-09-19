#!/usr/bin/python

import matplotlib.pyplot as plt
import argparse
import sys
import numpy
import basestats

def drawdata(args, data, stats):
    # A4 is 8.267 x 11.692 inches, so make it 10 inch wide..
    fig = plt.figure(figsize=(10, 5), dpi=80, facecolor='w', edgecolor='k')
    plt.hist(data, int(args.nbins) if args.nbins is not None else 100)
    
    if args.title is not None:
        plt.title(args.title)
                  
    if args.titlex is not None:
        plt.title(args.titlex + " (min: " + str(int(stats['min'])) + 
                                  ", mean: " + str(int(stats['mean'])) +
                                  ", median: " + str(stats['median']) + 
                                  ", max: " + str(stats['max']) + ")", fontsize=16)
    if (args.xlabel) is not None:
        plt.xlabel(args.xlabel)
    if (args.ylabel) is not None:
        plt.ylabel(args.ylabel)
    
    return fig

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--nbins',  help='number of bins')
    parser.add_argument('--title',  help='Title of the graph')
    parser.add_argument('--titlex', help='Title of the graph')
    parser.add_argument('--xlabel', help='X Axe label')
    parser.add_argument('--ylabel', help='Y Axe label')
    parser.add_argument('--onlypositive', action='store_true', help='Consider only positive numbers')
    parser.add_argument('--onlynegative', action='store_true', help='Consider only negative numbers')
    parser.add_argument('--saveas', default=None, help='Save figure as')

    args = parser.parse_args()

    inp = []
    fileinput=sys.stdin
    for line in sys.stdin:
        tails = line.strip().split()
        for tail in tails:
            inp.append(int(tail))

    if args.onlynegative is None and args.onlypositive is None:
        dta = inp
    if args.onlynegative is not None:
        dta = filter(lambda x: x <= 0, inp)
    if args.onlypositive  is not None:
        dta = filter(lambda x: x > 0, inp);

    stats = basestats.basestats(dta)
    if args.titlex is not None:
        print args.titlex
    if args.title is not None:
        print args.title
    print "------------------------"
    print "Card  : ", stats['card']
    print "Card  : ", stats['card']
    print "Min   : ", stats['min']
    print "Median: ", stats['median']
    print "Mean  : ", stats['mean']
    print "Max   : ", stats['max']
    print "Std   : ", stats['std']
    print "Var   : ", stats['var']
    print "------------------------"

    fig = drawdata(args, dta, stats)
    if args.saveas  is not None:
        fig.savefig(args.saveas + '.png', dpi=fig.dpi)

plt.show()