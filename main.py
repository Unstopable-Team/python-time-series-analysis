
# =============================================================================
# Import of Packages
# =============================================================================

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import wapi


# =============================================================================
# Data Visualization
# =============================================================================

identifier = 'pri_de_intraday_€_mwh_cet_min15_a.csv'

df = pd.read_csv('./data_base/{0}'.format(identifier), skiprows=1, names=['date', identifier])
print(df.head())

df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')
df.plot()
plt.show()

