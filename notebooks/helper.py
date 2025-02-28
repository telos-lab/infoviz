import os
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

import pandas as pd 
import seaborn as sns
import colorcet as cc

from infoviz.utils import set_rcParams

os.makedirs("../figures", exist_ok=True)

fontsize = 20
rcParams = {'figure.labelsize':fontsize, 'axes.labelsize':fontsize, 'xtick.labelsize':fontsize, 
            'ytick.labelsize':fontsize, 'legend.fontsize':fontsize, 'figure.titlesize':fontsize, 
            'legend.title_fontsize':fontsize, 
            'axes.titlesize':fontsize, 'legend.frameon':False}
set_rcParams(**rcParams)