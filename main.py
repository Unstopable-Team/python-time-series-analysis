
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
start = pd.Timestamp('2021-01-01 00:00')

# End date of data (last date is EXCLUDED!)
# end = pd.Timestamp('2021-03-20 00:00')
end = pd.to_datetime("now")


# =============================================================================
# name-identifier-mapping
# =============================================================================

name_dict = {
    'day-ahead-price'   : 'pri de spot €/mwh cet h a',
    'vmap'              : 'pri de intraday vwap id1 €/mwh cet h a',
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


# =============================================================================
# Data Visualization
# =============================================================================

quantity_1 = 'day-ahead-price'
quantity_2 = 'vmap'

curve_1 = session.get_curve(name=name_dict[quantity_1])
curve_2 = session.get_curve(name=name_dict[quantity_2])
# print(curve.curve_type)

df_1 = curve_1.get_data(data_from=start, data_to=end).to_pandas()
df_2 = curve_2.get_data(data_from=start, data_to=end).to_pandas()

print(df_1.head())

df_1.plot(figsize=(10,6))
df_2.plot(figsize=(10,6))
#plt.title(quantity)
plt.show()

