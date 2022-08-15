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

def epoch(raw, events_array=None, event_type='task', n_ms_windows=None, metadata=None):

    """ Epoch continuous data into events (trials if task data, n-second epochs if resting data)
    
        raw: MNE Raw object, either preprocessed already or not
        
        events_array: MNE-generated array of shape 3x[n_events], where the first column is the 
                      value of the event, the middle column is something (?), the last column 
                      is the timestamp of the event.
                      
                      If None, or if event_type =='rest', then an events array will be constructed using the n_ms_windows param such that 
                      the continuous data are sliced into evenly-spaced chunks.
                      
        event_type: str, option either 'task' or 'rest', this is only necessary so as to decide whether to use events_array to epoch or create our own events array
                      
        n_ms_wins: the width of the time windows to slice the data into, if it is un-event related data (e.g., resting state). Must be evenly divisible by the length of the timeseries 
                    
        metadata: string of filepath to behavioral logs metadata, in the form of CSV files; contains trial info. Per MNE requirements, the length of metadata must match n_epochs 

    
    """
    
    if event_type=='rest':
        events
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    