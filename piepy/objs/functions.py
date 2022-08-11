##### NOTE: Will need to account for micro/macro depth electrodes (micro electrodes within each probe should be its own electrode group)


def local_avg_reference(raw, elec_group_list, trig_list):
    """Rereference to local average of each depth or grid electrode
   
    Parameters
    ----------
    raw: Instance of MNE Raw Object
    elec_group_list: List of grouped electrodes (depth, grid, microwire, etc.). Should be output from sort channels function.
    trig_list: List of trigger channels marking events. Should be output from sort channels function.
    
    Returns
    -------
    reref_raw: MNE Raw Object
        Contains both non-iEEG channels and rereferenced electrode groups.
    """
    
    reref_elecs = [] # list to be populated with MNE raw objects that represent each rereferenced electrode group
    
    # MNE object that contains trigger channels
    trig_obj = raw.copy().pick_channels(trig_list, ordered=True)
    
    # loop through list of shanks
    for group in elec_group_list:
        print(group[0])
        elec_group_obj = raw.copy().pick_channels(group, ordered=True) # get selection of raw with shank channels
        elec_group_obj.set_eeg_reference('average') # rereference to average
        reref_elecs.append(elec_group_obj) # append to list of rereferenced shank objects
        
    # concatenate lists of rereferenced objects
    reref_raw = reref_elecs[0].add_channels(reref_elecs[1:])
    reref_raw = reref_raw.add_channels([trig_obj], force_update_info=True) # add non-iEEG channels
        
    return reref_raw


def bipolar_reference(raw, elec_group_list, trig_list):
    """Get bipolar referenced object (each channel is referenced to adjacent channels on the shank).
    
    Parameters
    ----------
    raw: Instance of MNE Raw Object
    elec_group_list: List of grouped electrodes (depth, grid, microwire, etc.). Should be output from sort channels function.
    trig_list: List of trigger channels marking events. Should be output from sort channels function.
    
    Returns
    -------
    reref_raw: MNE Raw Object
        Contains both non-iEEG channels and rereferenced electrode groups.
    """
    
    # copy of raw for bipolar
    raw_bip_ref = raw.copy()
    for group in elec_group_list:
        # get adjacent electode on shank
        raw_bip_ref = mne.set_bipolar_reference(raw_bip_ref, cathode=shank[0:-1], anode=shank[1:] )
        print(raw_bip_ref.info['ch_names'])
        
    return raw_bip_ref


def spatial_reference(raw, signal_range, noise_range):
    """"""
    raw_ssd = raw_annotate.copy().pick_types(seeg=True)
    ssd = mne.decoding.SSD(raw_ssd.info, 
                 filt_params_signal=dict(l_freq=signal[0], h_freq=signal[1], l_trans_bandwidth=1, h_trans_bandwidth=1),
                 filt_params_noise=dict(l_freq=noise[0], h_freq=noise[1], l_trans_bandwidth=1, h_trans_bandwidth=1),
                 reg='empirical', 
                 n_components=None, picks=None, sort_by_spectral_ratio=True,
                 return_filtered=False, n_fft=None, cov_method_params=None, rank=None)
    ssd.fit(X=raw_ssd.get_data())
    
    # Transform
    ssd_sources = ssd.transform(X=raw_ssd.get_data())
    
    # generate 
    
    return spatial_ref