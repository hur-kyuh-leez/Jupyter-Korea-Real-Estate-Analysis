import matplotlib as mpl
import numpy as np
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('fivethirtyeight')
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
# %matplotlib inline


# Take a look into csv file
df = pd.read_csv('data/data.csv')
df.date = pd.to_datetime(df.date, format='%Y%m')
df.index = df.date

df.head()

# modifying data
df.seoul_recuiting_number = df.seoul_recuiting_number[:'2018-01-01']
df.gangbook_price = df.gangbook_price[:'2018-01-01']
df.gangnam_price = df.gangnam_price[:'2018-01-01']
df['seoul_recuiting_number_gradient'] = np.gradient(df.seoul_recuiting_number)
df['gangbook_price_gradient'] = np.gradient(df.gangbook_price)
df['gangnam_price_gradient'] = np.gradient(df.gangnam_price)

df.head()

# Data exploration
fig = plt.figure(figsize=[15, 7])
plt.suptitle('Recruiting Number vs Real Estate Price', fontsize=22)
plt.subplot(211)
plt.plot(df.seoul_recuiting_number, 'red')
plt.legend()

plt.subplot(212)
gangbook_price, = plt.plot(df.gangbook_price, 'b')
plt.tick_params(axis='y')
plt.twinx()
gangnam_price, = plt.plot(df.gangnam_price, 'g')
plt.tick_params(axis='y')
plt.legend(handles=[gangnam_price, gangbook_price])
plt.tight_layout()
plt.show()


sns.factorplot('seoul_recuiting_number_gradient', 'gangbook_price_gradient',  data=df, size=6, aspect=2)
plt.show()
sns.factorplot('seoul_recuiting_number_gradient', 'gangnam_price_gradient', data=df, size=6, aspect=2)
plt.show()

