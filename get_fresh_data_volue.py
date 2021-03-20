
# =============================================================================
# Import of Packages
# =============================================================================

import numpy as np 
import pandas as pd 
import time 
import os 

import wapi


# =============================================================================
# Configuration
# =============================================================================

# Create a "data_base" folder, where the csv files will be saved
if os.path.isdir('data_base') is False:
    os.mkdir('data_base')

config_file = 'config.ini'
session = wapi.Session(config_file=config_file)


# =============================================================================
# Get Data from Volue
# API Wrapper: https://github.com/wattsight/wapi-python
# =============================================================================

#"""
# Define curve names
curve_names = [ # get day-ahead prices ? 
    'pri de intraday €/mwh cet min15 a',            # actual intraday prices
    'pri de imb stlmt €/mwh cet min15 a'            # imbalance price 
    'pri de intraday vwap €/mwh cet h a',           # volume weighted average price (vwap)
    'pri de intraday vwap id3 €/mwh cet min15 ca',  # vwap 3 h before delivery
    'pri de intraday vwap id1 €/mwh cet min15 ca',  # vwap 1 h before delivery
    'con de intraday mwh/h cet min15 a',            # actual consumption 
    'vol de imb sys mw cet min15 a'                 # system imbalance
]

# search for curves
curves = session.search(name=curve_names)
# curve = session.get_curve(name='pri de intraday €/mwh cet min15 a')
# print(curve.curve_type)

# Set up the event listener for the curves, which updates every 15 minutes
events = session.events(curves, timeout=15*60)

# Start timer
t_start = time.time()

# Loop through events
for e in events:

    if isinstance(e, wapi.events.EventTimeout):
        print('TIMEOUT!')

    elif isinstance(e, wapi.events.CurveEvent):
        print('New event in curve: ' + e.curve.name)
        curve = e.curve
        # get data for the last 24 h
        data_from = pd.Timestamp.now() - pd.Timedelta(hours=24)
        # get the TS object
        ts = curve.get_data(data_from=data_from)
        # convert to pandas Series
        data = ts.to_pandas()
        # get last timestep
        data_last = data.tail(1)

        # the name of the csv file for each curve is the curve name,
        # where the spaces and '/' are replaced by underscores
        csv_file = curve.name.replace(' ','_').replace('/','_')
        # we want the csv file to be in the "data_base" folder
        csv_file = os.path.join('data_base',csv_file)

        # Now write the last value to the csv file in 'append' mode
        data_last.to_csv(csv_file, mode='a', header=False)

    if (time.time() - t_start) > (60*60):
        # Stop code if no data was received for an hour
        break


# Adapted from: https://github.com/wattsight/wapi-python/blob/master/examples/Listening_for_changes/renewables_database.py 
