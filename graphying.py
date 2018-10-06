import matplotlib as mpl
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
df.Seeking_jobs_in_Seoul_numbers = df.Seeking_jobs_in_Seoul_numbers[:'2018-01-01']
df.gangbook_price = df.gangbook_price[:'2018-01-01']
df.gangnam_price = df.gangnam_price[:'2018-01-01']
df['Seeking_jobs_gradient'] = np.gradient(df.Seeking_jobs_in_Seoul_numbers)
df.head()

# plotting
fig = plt.figure(figsize=[15, 7])
plt.suptitle('Seeking Employement vs Real Estate Price', fontsize=22)
plt.subplot(211)
plt.plot(df.Seeking_jobs_in_Seoul_numbers, 'red')
plt.legend()

plt.subplot(212)
gangbook_price, = plt.plot(df.gangbook_price, 'b')
plt.tick_params(axis='y')
plt.twinx()
gangnam_price, =plt.plot(df.gangnam_price, 'g')
plt.tick_params(axis='y')
plt.legend(handles=[gangnam_price, gangbook_price])
plt.tight_layout()
plt.show()

sns.factorplot('Seeking_jobs_in_Seoul_numbers','gangnam_price', data=df, size=6, aspect=2)
plt.show()

sns.factorplot('Seeking_jobs_gradient','gangnam_price', data=df, size=6, aspect=2)
plt.show()