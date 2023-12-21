import matplotlib.pyplot as plt
import numpy as np
from statsmodels.tsa.stattools import adfuller

def generate_ar_process(lags, coefs, length):

    coefs = np.array(coefs)
    series = [np.random.normal() for _ in range(lags)]

    for _ in range(length):
        prev_vals = series[-lags:][::-1]
        new_val = np.sum(np.array(prev_vals) * coefs) + np.random.normal()
        series.append(new_val)
    return np.array(series)


def perform_adf_test(series):
    result = adfuller(series)
    print(result)
    print('ADF Statistic: %f' % result[0])
    print('p-value: %f' % result[1])


def generate_ar_3_process(length):
    coefs = [0.2, 0.1, 0.4]
    ar_3 = generate_ar_process(3, coefs, length)
    return ar_3


ar_3_process = generate_ar_3_process(1000)
perform_adf_test(ar_3_process)

plt.figure(figsize=(12, 4))
plt.plot(ar_3_process)
plt.title('AR(3) Process', fontsize=18)
plt.show()