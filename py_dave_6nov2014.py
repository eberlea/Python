# -*- coding: utf-8 -*-
"""
Created on Thu Nov  6 11:15:01 2014

@author: Annika
"""

import numpy as np 
from matplotlib import pyplot as plt

data = np.random.normal(1,1,10)

plt.plot(data)

#run script in terminal 
# cd \Python\scripts_with_dave
# ls
# ./simple_script.py # this will give error
# chmod u+x simple_script.py # change mode to make executable 
# ls -l # check to make sure executable
# ./simple_script.py