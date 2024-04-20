import numpy as np
from .metrics import r2_score


class LinearRegression:

    def __init__(self):
        """初始化Linear Regression模型"""
        self.coef_ = None
        self.intercept_ = None
        self._theta = None

    def fit_normal(self, X_train, y_train):
        """根据训练数据集X_train, y_train训练Linear Regression模型"""
        assert X_train.shape[0] == y_train.shape[0], \
            "the size of X_train must be equal to the size of y_train"

        X_b = np.hstack([np.ones((len(X_train), 1)), X_train])
        self._theta = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y_train)

        self.intercept_ = self._theta[0]
        self.coef_ = self._theta[1:]

        return self

    def predict(self, X_predict):
        """给定待预测数据集X_predict，返回表示X_predict的结果向量"""
        assert self.intercept_ is not None and self.coef_ is not None, \
            "must fit before predict!"
        assert X_predict.shape[1] == len(self.coef_), \
            "the feature number of X_predict must be equal to X_train"

        X_b = np.hstack([np.ones((len(X_predict), 1)), X_predict])
        return X_b.dot(self._theta)

    def score(self, X_test, y_test):
        """根据测试数据集 X_test 和 y_test 确定当前模型的准确度"""

        y_predict = self.predict(X_test)
        return r2_score(y_test, y_predict)

    def __repr__(self):
        return "LinearRegression()"

    def fit_gd(self, X_train, y_train, eta = 0.01, n_iters=1e4):
        assert X_train.shape[0] == y_train.shape[0], "The X_train's size should be equal to the y_train's size"
        def dJ(theta, X_b, y):
            #         res = np.zeros_like(theta)
            #        gd = np.zeros_like(theta)

            #        for i in range(len(theta)):
            #            if i == 0:
            #                gd[0] = np.sum((X_b.dot(theta) - y))
            #            else:
            #               gd[i] = np.sum((X_b.dot(theta) - y).dot(X_b[:, i]))
            #        return gd * 2 / len(X_b)
            return X_b.T.dot(X_b.dot(theta) - y) * 2. / len(X_b)



        def J(theta, X_b, y):
            try:
                return np.sum((X_b.dot(theta) - y) ** 2) / len(X_b)
            except:
                return float('inf')

        def gradient_descent(X_b, y, initial_theta, eta, n_iters, epsilon=1e-8):
            theta = initial_theta
            i_iter = 0

            while (i_iter < n_iters):
                last_theta = theta
                gradient = dJ(theta, X_b, y)
                theta = theta - eta*gradient
                if np.abs(J(theta, X_b, y) - J(last_theta, X_b, y)) < epsilon:
                    break
                i_iter += 1
            return theta

        X_b = np.hstack((np.ones((len(X_train), 1)), X_train))
        initial_theta = np.zeros(X_b.shape[1])
        self._theta = gradient_descent(X_b, y_train, initial_theta, eta, n_iters)
        self.coef_ = self._theta[1:]
        self.intercept_ = self._theta[0]
        return self