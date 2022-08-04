"""Class objects to wrap MNE object"""

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

import mne
import mne_bids

###################################################################################################
###################################################################################################

class iEEG:
    """contains MNE object of iEEG Raw and Preprocessed data
    Attributes
    ----------
    data: np array of data at current state (preprocessed vs. raw)
    history: dictionary of functions that have been called & their arguments
    channel_info: schema of channel locations (MNI, relative, groupings, etc, input by user)
    BIDSPath: importing from BIDS (like read_raw if they alreay have the iEEG-BIDS object for the user, otherwise writing to path)
    metadata: behavior
    info: history + filters + channel_info + epoch rejection metadata (iEEG.report?) -- What we add beyond MNE info
    MNE objects: pointer to class of MNE object (Raw, Epochs, Info)
    
    (import functions)
    triggers match metadata?
    import rereferencing
    import filter_line_noise
    import visualize
    
    Methods
    -------
    preprocess(reference, filter_line_noise, epoch, ...) <-- more automated, linear pipeline
        vizualize and confirm rereferencing
        PSD
    subfunctions of preprocess <-- can be called in isolation
    undo: undo previous step
        
    
    
    """
    data = np.array()
    info = None # to be populate with MNE info
    # potentially add electrode cluster type (depth, grid, microwire, high-density, etc.)
    ch_schema = {} # dictionary containing shank IDs & associated channel names
    history = {}
    
    
    def __init__(self, fname, subject, session=None, data_type=None, behavior=None):
        """Initialize object."""

        self.fname = fname
        self.subject = subject
        self.session = session
        self.data_type = data_type #resting, task
        self.behavior = behavior #csv of patient behavior (row = trial), plot trials that had poor performance (bonus)
        self.fs = None
        

    def load_data(self, self.fname):
        
    def sort_channels(self, self.ch_schema):
        
        # prompt user to sort their data (include in documentation)
        # per depth probe or grid, list all channels associated with that "cluster"? - point to tutorial/docs for details
        # depth/grid IDs and associated channels
        
    
        
    def preprocess(self, reference='average', filter_line_noise='spatial', epoch=True):
        
    def rereference(self, method='local_average'):
        
        if method == 'local_average': 
        
        if method == 'spatial':
            
        if method == 'bipolar':
            
        if method == 'global':
    
    def filter_data(self, filter_type='bandpass', frequency_range, filter_method='fir'): # add kwargs?
        
        if filter_type = 'bandpass':
        
        if filter_type = 'bandstop':
            
        if filter_type = 'highpass':
            
        if filter_type = 'lowpass':
        
        if filter_type = 'spatial':
            
    
    def epoch_data(self):
        
    def save_preprocessed_data(self, path):
    
        
################ organize later ####################    
    def apply_average_reference(): # check this - will the schema be contained in self?
        
    def apply_spatial_reference(montage):
        
    def apply_bipolar_reference():
        
    def apply_global_reference():
        
    def __add_to_history__():    
        
        
        
        
        