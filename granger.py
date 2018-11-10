from statsmodels.tsa.stattools import grangercausalitytests
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import matplotlib as mpl
mpl.use('TkAgg')
import pandas as pd






def normalization(array):
    """ scale data to 0~1"""

    y = np.array(array)
    y = y.reshape(-1, 1)
    min_max_scaler = MinMaxScaler()
    y = min_max_scaler.fit_transform(y)
    # checking if array contains NaN
    numpy_1 = np.array(array)
    if np.isnan(numpy_1).any():
        return None
    return y


# Find prior event
def granger(array1, array2):
    df = pd.DataFrame(normalization(array1))
    df['1'] = pd.DataFrame(normalization(array2))
    granger = grangercausalitytests(df, maxlag=18, verbose=True)
    min = 10
    best_lag = 0
    for i in granger:
        p_value = granger[i][0]['ssr_ftest'][1]
        if p_value < min:
            min = p_value
            best_lag = i
    return min, best_lag


#cleaning input data for def granger():
df = pd.read_csv('data/data.csv')
date = df['date'].values
gangnam_price = df['gangnam_price'].values
seoul_recuiting_number = df['seoul_recuiting_number'].values
seoul_recuiting_number = seoul_recuiting_number[np.logical_not(np.isnan(seoul_recuiting_number))]
min = min([len(seoul_recuiting_number), len(gangnam_price)])
seoul_recuiting_number = seoul_recuiting_number[:min]
gangnam_price = gangnam_price[:min]



if __name__== '__main__':
    granger(gangnam_price, seoul_recuiting_number)