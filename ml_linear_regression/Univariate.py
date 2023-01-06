import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from linear_regression import LinearRegression

data = pd.read_csv('...')

train_data = data.sample(frac=0.8)
test_data = data.drop(train_data.index)

input_name = '...'
output_name = '...'
x_train = train_data[[input_name]].values  # 传入数据应该为一个二维数组，一个样本特征应该是一个数组，而不是数值
y_train = train_data[[output_name]].values

x_test = test_data[[input_name]].values
y_test = test_data[[output_name]].values

plt.scatter(x_train, y_train, label='train')
plt.scatter(x_test, y_test, label='test')
plt.xlabel(input_name)
plt.ylabel(output_name)
plt.title('...')
plt.legend()
plt.show()

num_iterations = 500
learning_rate = 0.01

linear_regression = LinearRegression(x_train, y_train)
(theta, cost_history) = linear_regression.train(learning_rate, num_iterations)

print('开始时损失:', cost_history[0])
print('结束时损失：', cost_history[-1])
plt.plot(range(num_iterations), cost_history)
plt.xlabel('Iter')
plt.ylabel('cost')
plt.title('loss')
plt.show()

predictions_num = 100
x_predict = np.linspace(x_train.min(), x_train.max(), predictions_num).reshape(predictions_num,1)
y_predict = linear_regression.predict(x_predict)

plt.scatter(x_train, y_train, label='train')
plt.scatter(x_test, y_test, label='test')
plt.plot(x_predict, y_predict, 'r', label='predict')
plt.xlabel(input_name)
plt.ylabel(output_name)
plt.title('...')
plt.legend()
plt.show()
