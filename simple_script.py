#!/usr/bin/env python
# encoding: utf-8
"""
simple_script.py - generate some random data and then plot a histogram

Created on Thu Nov  6 11:27:43 2014

@author: Annika
"""
import matplotlib.pyplot as plt
import numpy as np

data = np.random.gumbel(1,1,500000)
plt.hist(data,100)
plt.show()