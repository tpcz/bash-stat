#!/usr/bin/python

import matplotlib.pyplot as plt
import argparse
import sys
import numpy

def basestats(dta):
    mean=numpy.mean(dta)
    median=numpy.median(dta)
    maxx=max(dta)
    minn=min(dta)
    std=numpy.std(dta)
    var=numpy.var(dta)
    card=len(dta)
    return {'card':card, 'mean': mean, 'max':maxx, 'min':minn, 'median':median, 'std':std, 'var':var}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--onlypositive', help='Consider only positive numbers')
    parser.add_argument('--onlynegative', help='Consider only negative numbers')
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

    stats = basestats(dta) 

    print "Card  : ", stats['card']
    print "Min   : ", stats['min']
    print "Median: ", stats['median']
    print "Mean  : ", stats['mean']
    print "Max   : ", stats['max']
    print "Std   : ", stats['std']
    print "Var   : ", stats['var']
    