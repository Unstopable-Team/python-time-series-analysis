
# =============================================================================
# Import of Packages
# =============================================================================

import numpy as np 
import pandas as pd 

import wapi
from entsoe import EntsoeRawClient, EntsoePandasClient


# =============================================================================
# Cofiguration
# =============================================================================

start = pd.Timestamp('20201201', tz='Europe/Berlin')
end = pd.Timestamp('20210101', tz='Europe/Berlin')
country_code = 'DE'  # Germany


# =============================================================================
# Get Data from Volue
# API Wrapper: https://github.com/wattsight/wapi-python
# =============================================================================

#"""
config_file_path = 'config.ini'
session = wapi.Session(config_file=config_file_path)

# Define curve names
curve_names = [ # get day-ahead prices ? 
    'pri de intraday €/mwh cet min15 a',            # actual intraday prices
    'pri de imb stlmt €/mwh cet min15 a'            # imbalance price 
    'pri de intraday vwap €/mwh cet h a',           # volume weighted average price (vwap)
    'pri de intraday vwap id3 €/mwh cet min15 ca',  # vwap 3 h before delivery
    'pri de intraday vwap id1 €/mwh cet min15 ca'   # vwap 1 h before delivery
]


curve = session.get_curve(name='pri de intraday €/mwh cet min15 a')
# print(curve.curve_type)

ts = curve.get_data(data_from=start, data_to=end)

df = ts.to_pandas()
print(df.head())
#"""


# =============================================================================
# Get Data from Entso-E
# API Wrapper: https://github.com/EnergieID/entsoe-py
# =============================================================================

"""
key = str(np.genfromtxt('entsoe.txt',dtype='str'))
client = EntsoePandasClient(api_key=key)


# Time Series

# NoMatchingDataError
# ts_day_ahead = client.query_day_ahead_prices(country_code, start=start,end=end)

ts_load = client.query_load(country_code, start=start,end=end)

ts_load_forecast = client.query_load_forecast(country_code, start=start,end=end)

ts_generation_forecast = client.query_generation_forecast(country_code, start=start,end=end)


# Dataframes

df_wind_and_solar_forecast = client.query_wind_and_solar_forecast(country_code, start=start,end=end, psr_type=None)

df_generation = client.query_generation(country_code, start=start,end=end, psr_type=None)

df_installed_generation_capacity = client.query_installed_generation_capacity(country_code, start=start,end=end, psr_type=None)

df_crossborder_flows = client.query_crossborder_flows('DE', 'DK', start=start,end=end)

# BadRequest: 
# df_imbalance_prices = client.query_imbalance_prices(country_code, start=start,end=end, psr_type=None)

# BadRequest: 
# df_unavailability_of_generation_units = client.query_unavailability_of_generation_units(country_code, start=start,end=end, docstatus=None)

# BadRequest: 
# df_withdrawn_unavailability_of_generation_units = client.query_withdrawn_unavailability_of_generation_units('DE', start=start,end=end)

# ts.to_csv('outfile.csv')
#"""

