
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets

def set_rcParams(**kwargs):
    plt.rcParams['pdf.fonttype'] = 42
    plt.rcParams['text.usetex'] = True
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['text.latex.preamble'] = r"\usepackage{amssymb}\usepackage{amsmath}\usepackage{times}"
    for k, v in kwargs.items():
        try:
            plt.rcParams[k] = v
        except KeyError:
            pass

def load_df(dataset:str):
    if dataset == "iris":
        ds = datasets.load_iris(as_frame=True)
    if dataset == "california_housing":
        ds = datasets.fetch_california_housing(as_frame=True)
    df = ds["frame"]
    target_names = ds.target_names
    feature_names = ds.feature_names
    if len(target_names) > 1: 
        df.rename(columns=dict(target="y"), inplace=True)
        df["y_name"] = df.y.map(lambda x:target_names[x])
    else: 
        df.rename(columns={target_names[0]:"y"}, inplace=True)
        df["y_name"] = target_names[0]
    return df