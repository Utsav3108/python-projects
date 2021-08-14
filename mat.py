#Three lines to make our compiler able to draw:
import sys
import matplotlib
matplotlib.use('TkAgg')

import pandas as pd
import matplotlib.pyplot as plt
dic = {
    'Year':[2017,2018,2020,2021],
    'Price':[100000,123000,154786,20000],
    'Car':'Bmw',
    }
df = pd.DataFrame(dic)

df.plot()

plt.show()

# Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()