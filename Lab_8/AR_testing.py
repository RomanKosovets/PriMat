from AR_generate import *
from statsmodels.tsa.arima.model import ARIMA

data = generate_ar_3_process(1000)
train_data = data[:803]
test_data = data[803:]
print(data.shape, train_data.shape, test_data.shape)

# Чем более поздний промежуток времени мы пытаемся предсказать, тем хуже получаются наши предсказания. Наши предсказания сводятся к мат. ожиданию нашего временного ряда, что является не интересной для нас информацией

# model = ARIMA(train_data, order=(3, 0, 0))
# model_fit = model.fit()
# print(model_fit.summary())
# predictions = model_fit.predict(start=len(train_data), end=len(train_data)+len(test_data) - 1, dynamic=False)
# residuals = test_data - predictions

# Чтобы избежать деградации предсказаний к мат. ожиданию, воспользуемся окном предсказаний. По сути мы будем предсказывать не сразу на большой промежуток времени, а частями.
# т.е. Мы хотим предсказать 3 будущих точки времени, для этого сделаем следующее:
#
# Обучим модель на месяцах 1, 2, ..., k-3 -> предскажем k-2
# Обучим модель на месяцах 1, 2, ..., k-3, k-2 -> предскажем k-1
# Обучим модель на месяцах 1, 2, ..., k-3, k-2, k-1 -> предскажем k
#
# Таким образом мы получим лучший результат предсказаний, т.к. теперь мы не пытаемся сразу предсказать далеко в будущее, а предсказываем лишь небольшими частями вперёд.


predictions = []
windowSize = 10
for i in range(len(train_data), len(train_data)+len(test_data) - 1, windowSize):
    train_data = data[:i]
    model = ARIMA(train_data, order=(3,0,0))
    model_fit = model.fit()
    pred = model_fit.predict(start=i, end=i+windowSize - 1, dynamic=False)
    for i in range(len(pred)):
        predictions.append(pred[i])

plt.figure(figsize=(10,4))
plt.plot(test_data)
plt.plot(predictions)
plt.legend(('Data', 'Predictions'), fontsize=16)
plt.title('First Difference of fish Sales', fontsize=20)
plt.ylabel('Sales', fontsize=16)
plt.show()
