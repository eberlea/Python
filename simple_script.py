#!/usr/bin/env python
# encoding: utf-8
"""
simple_script.py - generate some random data and then plot a histogram

Created on Thu Nov  6 11:27:43 2014

@author: Annika
"""
import matplotlib.pyplot as plt
import numpy as np

def show_bryant(data_length=500000, bins=100):
    """ Create some data with the gumbel distribution, then plot as a historgram
    Takes: 
        data_length: how many points to generate
        bins: how many bins to sort data into for histogram
    Gives:
        None 
    """
    data = np.random.gumbel(1,1,data_length)
    plt.hist(data,bins)
    plt.show()
    
def main():
    show_bryant(10000,50)

if __name__ == '__main__':
    main()