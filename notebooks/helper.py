import os
import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd 
import seaborn as sns
import colorcet as cc

from infoviz.utils import set_rcParams

fontsize = 20
rcParams = {'figure.labelsize':fontsize, 'axes.labelsize':fontsize, 'xtick.labelsize':fontsize, 
            'ytick.labelsize':fontsize, 'legend.fontsize':fontsize, 'figure.titlesize':fontsize, 
            'axes.titlesize':fontsize, 'legend.frameon':False}
set_rcParams(**rcParams)