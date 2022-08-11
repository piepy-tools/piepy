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
        """ Prompts user to manually sort their data channels by depth/grid/microwire 
        Parameters
        ----------
        Returns
        -------
        """
        
        elec_group_type = ''
        
        grid_chans = ''
        strip_chans = ''
        depth_chans = ''
        microwire_chans = ''
        
        cluster_list = []
        aux_chans = ''
        aux_list = []
        proceed = 'n'
        proceed_aux = 'n'

        print('In this step, sort all the channels in your data into their\
        respective electrode groups. Electrodes can be grouped by grid, strip,\
        depth probe, or microwire array. For more details about electrode group\
        types, refer to the "Glossary of Electrode Types" on the piepy repository\
        on Github.\
        \n\n First ')
        
        print('printing all channels...')

        ch_names = raw.info['ch_names']
        print(ch_names)
        print('\n\n')


        print('enter all iEEG channels on each cluster (depth probe/grid/microwire)\
               as a list of strings (without brackets), excluding non-iEEG channels.\
               When done, type done. \n')

        while proceed=='n':
            while cluster_chans != 'done':
                cluster_ids = input('cluster id/name: '
                cluster_chans = input('channels in cluster: ');
                if cluster_chans != 'done':
                    cluster_chans = list(eval(cluster_chans))
                    cluster_list.append(cluster_chans)
                else:
                    break
            
            print('\n Here are your channels grouped by cluster.\
                   Visually inspect them to make sure they were input correctly. \n')
            
            print(cluster_list)
            proceed = input('Continue? (y/n)')
            assert proceed == 'y' or proceed == 'n'

        print('\n enter each auxillary channel (non-iEEG, stimulus, trigger, ECG,\
               etc.)\ one at a time as a string. When done, type done')

        while proceed_aux == 'n':
            while aux_chans != 'done':
                aux_chans = input('trigger/auxillary channel:');
                if aux_chans != 'done':

                    try:
                        eval(aux_chans)
                    except:
                        print('unable to interpret.\
                               please make sure channel name is a string')
                        break

                    aux_chans = eval(aux_chans)

                    assert isinstance(aux_chans,str), 'please enter each channel name separately'
                    assert aux_chans in raw.info['ch_names'], 'channel not found in raw object'

                    aux_list.append(aux_chans)

                else:
                    break

    
        print('\n Here are your non-iEEG channels. Any channels not included\
               in these two lists will not be included in further preprocessing\
               steps.\n')
        print(aux_list)
        proceed_aux = input('Continue? (y/n)')
        assert proceed_aux == 'y' or proceed_aux == 'n'

    return shank_list, trig_list
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
        
        
        
        
        