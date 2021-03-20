
# =============================================================================
# Import of Packages
# =============================================================================

import numpy as np 
import pandas as pd 

import wapi
from entsoe import EntsoeRawClient, EntsoePandasClient


# =============================================================================
# Get Data from Volue
# API Wrapper: https://github.com/wattsight/wapi-python
# =============================================================================

"""
config_file_path = 'config.ini'
session = wapi.Session(config_file=config_file_path)


curve = session.get_curve(name='pri de intraday €/mwh cet min15 a')
# print(curve.curve_type)

ts = curve.get_data(data_from='2018-01-01T14:00Z', data_to='2018-02-01T14:00Z')

df = ts.to_pandas()
print(df.head())
#"""


# =============================================================================
# Get Data from Entso-E
# API Wrapper: https://github.com/EnergieID/entsoe-py
# =============================================================================

#"""
key = str(np.genfromtxt('entsoe.txt',dtype='str'))
client = EntsoePandasClient(api_key=key)

start = pd.Timestamp('20171201', tz='Europe/Brussels')
end = pd.Timestamp('20180101', tz='Europe/Brussels')
country_code = 'BE'  # Belgium

ts = client.query_day_ahead_prices(country_code, start=start,end=end)
ts.to_csv('outfile.csv')
#"""

