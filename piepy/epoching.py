## Aug 11 2022: first attempt for piepy toolbox for developing function that epochs
## import data that Sydney uploaded to google drive using BIDSpath


# imports
import os
import numpy as np
import scipy.io as sio
import scipy as sp
import pandas as pd

import mne
import mne_bids
from mne_bids import stats

import matplotlib.pyplot as plt
# allows for interactive window
%matplotlib qt 

def epoch(data, events_array):

    """ Epoch continuous data into events (trials if task data, n-second epochs if resting data)
    
        data: MNE raw object, either preprocessed already or not

    
    """