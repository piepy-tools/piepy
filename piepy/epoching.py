## Aug 11 2022: first attempt for piepy toolbox for developing function that epochs
## import data that Sydney uploaded to google drive using BIDSpath


#####################
#                   #
#   GIT PULL FIRST  #
#                   #
#####################


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

def epoch(raw, events_array=None, event_type='task', n_windows=None, metadata=None):

    ## Syd's note: we should make the epochs optional, so when integrating with the main preprocessing function, set epoching == True or False

    ## what we're adding on top of the MNE epoching is? 
    ##     -- The checking of csv data compatibility before data entry
    ##     -- For resting-state data, create the epochs events array for you
    ##     -- cleaning epochs automatically ?
    ##     -- If there's not an events_array from the BIDS object, or because it's resting state data, try creating one

    """ Epoch continuous data into events (trials if task data, n-second epochs if resting data)
    
        raw: MNE Raw object, either preprocessed already or not
        
        events_array: MNE-generated array of shape 3x[n_events], where the first column is the 
                      value of the event, the middle column is something (?), the last column 
                      is the timestamp of the event.
                      
                      If None, or if event_type =='rest', then an events array will be constructed using the n_ms_windows param such that 
                      the continuous data are sliced into evenly-spaced chunks.
                      
        event_type: str, option either 'task' or 'rest', this is only necessary so as to decide whether to use events_array to epoch or create our own events array
                      
        n_windows: the width of the time windows to slice the data into, if it is un-event related data (e.g., resting state). Must be evenly divisible by the length of the timeseries 
                    
        metadata: string of filepath to behavioral logs metadata, in the form of CSV files; contains trial info. Per MNE requirements, the length of metadata must match n_epochs 


    Attributes
    ----------    
    
    continuous : MNE object of continuous, un-epoched data 





    """

    raw.load_data()
    
    if event_type=='rest':
        # if the events type is rest, then the events array is going to just chunk the data up into 
        # arbitrary windows that are divisible with the length of the data

        n_times = len(raw.times)

        try:
            assert ((n_times%n_windows) > 0), 'the length of data must be evenly divisible by n_windows'
        except AssertionError as msg:
            print(msg)

        if 


        events_array = np.array()

        


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
