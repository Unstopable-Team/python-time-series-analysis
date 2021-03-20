
# =============================================================================
# Import of Packages
# =============================================================================

import numpy as np 
import wapi


# =============================================================================
# Get Data from Volue
# =============================================================================

config_file_path = 'config.ini'
session = wapi.Session(config_file=config_file_path)


curve = session.get_curve(name='pri de intraday €/mwh cet min15 a')
# print(curve.curve_type)

ts = curve.get_data(data_from='2018-01-01T14:00Z', data_to='2018-02-01T14:00Z')

df = ts.to_pandas()
print(df.head())
