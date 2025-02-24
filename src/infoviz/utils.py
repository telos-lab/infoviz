
import matplotlib.pyplot as plt

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
