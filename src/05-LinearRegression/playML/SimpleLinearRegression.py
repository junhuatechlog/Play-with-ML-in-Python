import numpy as np

class SimpleLinearRegression:

    def __init__(self):
        self.a_ = None
        self.b_ = None
        self.len_ = None


    def fit(self, x_train, y_train):
        assert x_train.ndim == 1, "The regressor only support simple feature training data!"
        assert len(x_train) == len(y_train), "The size of x_train and y_train must be equal!"
        x_mean = np.mean(x_train)
        y_mean = np.mean(y_train)
        numerator = (x_train - x_mean).dot(y_train - y_mean)
        denominator = np.sum((x_train - x_mean)**2)
        self.a_ = numerator/denominator
        self.b_ = y_mean - (self.a_*x_mean)
        self.len_ = len(x_train)
        #print("parameter: ", self.a_, self.b_, self.len_)
        return self


    def predict(self, x_predict):
        assert x_predict.ndim == 1, "The regressor only support simple feature training data!"
        assert self.a_ is not None and self.b_ is not None, "Fit must be executed before call the predict!"
        return np.array([self._predict(x) for x in x_predict])


    def _predict(self, x_single):
        return x_single * self.a_ + self.b_

    def __repr__(self):
        return "Simple Linear Regression!"
