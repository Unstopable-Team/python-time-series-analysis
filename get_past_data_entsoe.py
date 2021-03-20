
# =============================================================================
# Import of Packages
# =============================================================================

import numpy as np 
import pandas as pd
import os  

from entsoe import EntsoeRawClient, EntsoePandasClient


# =============================================================================
# Cofiguration
# =============================================================================

start = pd.Timestamp('20180101', tz='Europe/Berlin')
end = pd.Timestamp('20210320', tz='Europe/Berlin')
country_code = 'DE'  # Germany

# Create a "data_base" folder, where the csv files will be saved
if os.path.isdir('data_base') is False:
    os.mkdir('data_base')


# =============================================================================
# Get Data from Entso-E
# API Wrapper: https://github.com/EnergieID/entsoe-py
# =============================================================================

#"""
key = str(np.genfromtxt('entsoe.txt',dtype='str'))
client = EntsoePandasClient(api_key=key)


# Time Series

# NoMatchingDataError
# ts_day_ahead = client.query_day_ahead_prices(country_code, start=start,end=end)

ts_load = client.query_load(country_code, start=start,end=end)
ts_load.to_csv('data_base/ts_load.csv')

ts_load_forecast = client.query_load_forecast(country_code, start=start,end=end)
ts_load_forecast.to_csv('data_base/ts_load_forecast.csv')

ts_generation_forecast = client.query_generation_forecast(country_code, start=start,end=end)
ts_generation_forecast.to_csv('data_base/ts_generation_forecast.csv')


# Dataframes

df_wind_and_solar_forecast = client.query_wind_and_solar_forecast(country_code, start=start,end=end, psr_type=None)
df_wind_and_solar_forecast.to_csv('data_base/df_wind_and_solar_forecast.csv')

df_generation = client.query_generation(country_code, start=start,end=end, psr_type=None)
df_generation.to_csv('data_base/df_generation.csv')

df_installed_generation_capacity = client.query_installed_generation_capacity(country_code, start=start,end=end, psr_type=None)
df_installed_generation_capacity.to_csv('data_base/df_installed_generation_capacity.csv')

df_crossborder_flows = client.query_crossborder_flows('DE', 'DK', start=start,end=end)
df_crossborder_flows.to_csv('data_base/df_crossborder_flows.csv')


# df_imbalance_prices = client.query_imbalance_prices(country_code, start=start,end=end, psr_type=None)
# df_imbalance_prices.to_csv('data_base/df_imbalance_prices.csv')

# BadRequest: 
# df_unavailability_of_generation_units = client.query_unavailability_of_generation_units(country_code, start=start,end=end, docstatus=None)

# BadRequest: 
# df_withdrawn_unavailability_of_generation_units = client.query_withdrawn_unavailability_of_generation_units('DE', start=start,end=end)

# ts.to_csv('outfile.csv')
#"""
