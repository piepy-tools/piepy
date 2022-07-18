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

    def __init__(self, center_extrema='trough', find_extrema_kwargs=None):
        """Initialize object."""

        # Settings
        self.center_extrema = center_extrema

        if find_extrema_kwargs is None:
            self.find_extrema_kwargs = {'filter_kwargs': {'n_cycles': 3}}
        else:
            self.find_extrema_kwargs = find_extrema_kwargs

        # Fit params
        self.sig = None
        self.fs = None
        self.f_range = None
        self.std = None

        # Results
        self.df_features = None
        self.spikes = []
        self.params = None
        self.spikes_gen = None


    def __len__(self):
        """Define the length of the object."""

        return len(self.spikes)


    def __iter__(self):
        """Allow for iterating across the object."""

        for spike in self.spikes:
            yield spike[~np.isnan(spike)]


    def __getitem__(self, index):
        """Allow for indexing into the object."""

        return self._spikes[index]