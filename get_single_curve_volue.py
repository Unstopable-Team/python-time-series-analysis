
# =============================================================================
# Import of Packages
# =============================================================================

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
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
end = pd.Timestamp('2021-03-20 00:00')


# =============================================================================
# Get Data from Volue
# API Wrapper: https://github.com/wattsight/wapi-python
# =============================================================================

curve = session.get_curve(name='pri de imb stlmt €/mwh cet min15 s')
# print(curve.curve_type)

df_1 = curve.get_data(data_from='2020-01-01T14:00Z', data_to='2021-02-01T14:00Z')

df = ts.to_pandas()
print(df.head())

df.plot(figsize=(10,6))
plt.show()


# Adapted from: https://wattsight-wapi-python.readthedocs-hosted.com/en/latest/curves.html
