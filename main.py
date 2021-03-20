
# =============================================================================
# Import of Packages
# =============================================================================

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import wapi


# =============================================================================
# Configuration
# =============================================================================

config_file = 'config.ini'
session = wapi.Session(config_file=config_file)

# Start Date of data
start = pd.Timestamp('2020-01-01 00:00')

# End date of data (last date is EXCLUDED!)
# end = pd.Timestamp('2021-03-20 00:00')
end = pd.to_datetime("now")


# =============================================================================
# name-identifier-mapping
# =============================================================================

name_dict = {
    'day-ahead-price'   : 'pri de spot €/mwh cet h a',
    'vmap'              : 'pri de intraday vwap €/mwh cet h a',
    'vmap-id1'          : 'pri de intraday vwap id1 €/mwh cet h a',
    'vmap-id3'          : 'pri de intraday vwap id3 €/mwh cet h a',
    'imbalance-price'   : 'pri de imb stlmt €/mwh cet min15 s',
    'grid-imbalance'    : 'pri cwe imb stlmt igcc €/mwh cet min15 s',
    'nuclear-prod'      : 'pro de nuc mwh/h cet h af',
    'nuclear-capacity'  : 'cap de nuc mw cet h af',
    'coal-prod'         : 'pro de thermal coal mwh/h cet min15 a',
    'coal-capacity'     : 'cap de avail thermal coal mw cet h f',
    'lignite-prod'      : 'pro de thermal lignite mwh/h cet min15 a',
    'lignite-capacity'  : 'cap de avail thermal lignite mw cet h f',
    'gas-prod'          : 'pro de thermal gas mwh/h cet min15 a',
    'gas-capacity'      : 'cap de avail thermal gas mw cet h f',
    'wind-actual'       : 'pro de wnd mwh/h cet min15 a',
    'wind-normal'       : 'pro de wnd mwh/h cet min15 n',
    'solar-actual'      : 'pro de spv mwh/h cet min15 a',
    'solar-normal'      : 'pro de spv mwh/h cet min15 n',
    'consumption-actual': 'con de mwh/h cet min15 a',
    'consumption-normal': 'con de mwh/h cet min15 n',
    'temp-normal'       : 'tt de con °c cet min15 n'
}

def get_pandas_data(quantity_name, start=start, end=end, session=session, name_dict=name_dict):
    """Obtains a pandas dataframe for a given quantity from the volue API."""

    curve = session.get_curve(name=name_dict[quantity_name])
    df = curve.get_data(data_from=start, data_to=end).to_pandas()

    return(df)


# =============================================================================
# Absolute Price Change
# =============================================================================

day_ahead_price = get_pandas_data('vmap')
intra_day_price = get_pandas_data('vmap-id1')

absolute_price_change = intra_day_price.subtract(day_ahead_price)
absolute_price_change = absolute_price_change.abs()

def get_correlation(quantity_name, absolute_price_change=absolute_price_change):
    quantity_df = get_pandas_data(quantity_name)

    print("Correlation with {0}: ".format(quantity_name), quantity_df.corr(absolute_price_change))

def get_df_correlation(quantity_df, absolute_price_change=absolute_price_change):

    print("Correlation with {0}: ".format(quantity_df.name), quantity_df.corr(absolute_price_change))


"""
# day_ahead_price.plot(figsize=(10,6))
# intra_day_price.plot(figsize=(10,6))
absolute_price_change.plot(figsize=(10,6))
# plt.title('absolute price change')
plt.show()
#"""

# "major impact events" are marked by a minimum 100 % relative change between day ahead and intraday price
# the question is: how do these events correlated with impact factors, such as 
# - large amount of wind / sunshine 
# - production by different types 
# - consumption


# =============================================================================
# Correlation with Wind
# =============================================================================

#"""
wind_actual = get_pandas_data('wind-actual')
wind_normal = get_pandas_data('wind-normal')
absolute_wind_strength = wind_actual.subtract(wind_normal)

get_df_correlation(absolute_wind_strength)
#"""


# =============================================================================
# Correlations with single variables
# =============================================================================

#"""
get_correlation('imbalance-price')
get_correlation('grid-imbalance')
get_correlation('consumption-actual')
#"""


# =============================================================================
# Correlation with Renewables
# =============================================================================

nuclear_prod = get_pandas_data('nuclear-prod')
coal_prod = get_pandas_data('coal-prod')
lignite_prod = get_pandas_data('lignite-prod')
gas_prod = get_pandas_data('gas-prod')

wind_actual = get_pandas_data('wind-actual')
solar_actual = get_pandas_data('solar-actual')

total_renewable = solar_actual.add(wind_actual)
total_nonrenewable = nuclear_prod.add(coal_prod).add(lignite_prod).add(gas_prod)
share_of_renewables = total_renewable.divide(total_renewable.add(total_nonrenewable))

get_df_correlation(total_renewable)
get_df_correlation(total_nonrenewable)
get_df_correlation(share_of_renewables)


"""
# wind_actual.plot(figsize=(10,6))
absolute_price_change.plot(figsize=(10,6))
#consumption_actual.plot(figsize=(10,6))
# plt.title('absolute price change')
plt.show()
#"""