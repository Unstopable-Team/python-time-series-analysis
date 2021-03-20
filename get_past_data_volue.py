
# =============================================================================
# Import of Packages
# =============================================================================

import numpy as np 
import pandas as pd 
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

# Start Date of data
start = pd.Timestamp('2018-01-01 00:00')

# End date of data (last date is EXCLUDED!)
# end = pd.Timestamp('2021-03-20 00:00')
end = pd.to_datetime("now")


# =============================================================================
# Get Data from Volue
# API Wrapper: https://github.com/wattsight/wapi-python
# =============================================================================

#"""
# Define curve names
curve_names = [
    'pri de spot €/mwh cet h a',                    # day-ahead prices
    'pri de intraday €/mwh cet h a',                # actual intraday prices
    'pri de intraday vwap €/mwh cet h a',           # volume weighted average price (vwap)
    'pri de intraday vwap id3 €/mwh cet h ca',      # vwap 3 h before delivery
    'pri de intraday vwap id1 €/mwh cet h ca',      # vwap 1 h before delivery
    'pri de imb stlmt €/mwh cet min15 s'            # imbalance price 
    'pri cwe imb stlmt igcc €/mwh cet min15 s'      # grid imbalance
    'con de mwh/h cet min15 a',                     # actual consumption 
]

for curve_name in curve_names:

    # init empty df for each curve
    df = pd.DataFrame()

    # get curve data and convert to pandas series
    
    print('Fetching curve', curve_name)

    try:
        curve = session.get_curve(name=curve_name)
    except wapi.session.MetadataException:
        continue

    try:
        ts = curve.get_data(data_from=start, data_to=end)
    except AttributeError:
        ts = curve.get_instance(issue_date=start)

    s = ts.to_pandas()

    # add data to curve dataframe
    df[curve_name] = s

    # create valid name for saving to csv
    csv_name = curve_name.replace('  ',' ').replace(' ','_').replace('/','_')

    # save to comma separated csv with point as decimal separator
    df.to_csv(os.path.join('data_base',csv_name+'.csv'))


# Adapted from: https://github.com/wattsight/wapi-python/blob/master/examples/Timeseries_curve_examples/ts_get_multiple_curves.py
#"""


# =============================================================================
# Plot Data as Example
# =============================================================================

"""
identifier = 'pri de spot €/mwh cet h a'
df = pd.read_csv('./data_base/{0}'.format(identifier), skiprows=1, names=['date', identifier])
print(df.head())

df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')
df.plot()
plt.show()
#"""