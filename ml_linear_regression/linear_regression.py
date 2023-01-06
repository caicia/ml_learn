import numpy as np
from ml_linear_regression import prepare_for_training


class LinearRegression:

    def __init__(self, data, labels, polynomial_degree=0, sinusoid_degree=0, normalize_data=True):
        """
            对数据进行预处理
            先得到所有的特征个数
            初始化参数矩阵
        """
        (
            data_processed,
            features_mean,
            features_deviation
        ) = prepare_for_training(data, polynomial_degree, sinusoid_degree, normalize_data)

        self.data = data_processed
        self.labels = labels
        self.features_mean = features_mean
        self.features_deviation = features_deviation
        self.polynomial_degree = polynomial_degree
        self.sinusoid_degree = sinusoid_degree
        self.normalize_data = normalize_data

        num_features = self.data.shape[1]  # 知道有多少列（就是多少个特征），不关心多少个样本
        self.theta = np.zeros((num_features, 1))

    def train(self, learning_rate, num_iterations=500):
        cost_history = self.gradient_descent(learning_rate, num_iterations)  # 更新损失值的同时，更新theta
        return self.theta, cost_history

    def gradient_descent(self, learning_rate, num_iterations):
        cost_history = []  # 记录损失的变化
        for _ in range(num_iterations):
            self.gradient_step(learning_rate)
            cost_history.append(self.cost_function(self.data, self.labels))

        return cost_history

    def gradient_step(self, learning_rate):
        """
        梯度下降参数更新计算方法
        :param learning_rate:
        :return:
        """
        num_examples = self.data.shape[0]  # 样本数量
        prediction = LinearRegression.hypothesis(self.data, self.theta)
        delta = prediction - self.labels
        theta = self.theta
        theta = theta - learning_rate * (1 / num_examples) * (
            np.dot(delta.T, self.data)).T  # 梯度下降公式，转置是为了矩阵运算代替for循环，第二个转置是为了展示方便
        self.theta = theta

    @staticmethod
    def hypothesis(data, theta):
        predictions = np.dot(data, theta)
        return predictions

    def cost_function(self, data, labels):
        num_examples = data.shape[0]
        prediction = LinearRegression.hypothesis(self.data, self.theta)
        delta = prediction - self.labels

        cost = (1 / 2) * np.dot(delta.T, delta) / num_examples  # 选择合适的损失函数
        return cost[0][0]  # 需要的函数损失值

    def get_cost(self, data, labels):
        data_processed = prepare_for_training(data, self.polynomial_degree, self.sinusoid_degree, self.normalize_data)[0]
        return self.cost_function(data_processed, labels)

    def predict(self, data):
        data_processed = prepare_for_training(data, self.polynomial_degree, self.sinusoid_degree, self.normalize_data)[0]
        predictions = LinearRegression.hypothesis(data_processed, self.theta)
        return predictions
