
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
start = pd.Timestamp('2021-03-01 00:00')

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
    'wind-forecast-1'   : 'pro de wnd ec00 mwh/h cet min15 f'
    'wind-normal'       : 'pro de wnd mwh/h cet min15 n',
    'solar-actual'      : 'pro de spv mwh/h cet min15 a',
    'solar-normal'      : 'pro de spv mwh/h cet min15 n',
    'solar-forecast'    : 'pro de spv ec00 mwh/h cet min15 f',
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
# Relative Price Change
# =============================================================================

day_ahead_price = get_pandas_data('day-ahead-price')
intra_day_price = get_pandas_data('vmap')

absolute_price_change = intra_day_price.subtract(day_ahead_price)
relative_price_change = absolute_price_change.divide(day_ahead_price)

max_relative_price_change = relative_price_change[relative_price_change > 0.1]
min_relative_price_change = relative_price_change[relative_price_change < -0.1]


relative_price_change.plot()
max_relative_price_change.plot(marker='o', c='r', ls='')
min_relative_price_change.plot(marker='o', c='g', ls='')
plt.ylim(-0.5,0.5)
plt.show()


# Indicator: High Imbalance Price

# Indicator: Increase in Renewable Energies


