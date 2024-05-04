import numpy as np
from math import sqrt


def accuracy_score(y_true, y_predict):
    """计算y_true和y_predict之间的准确率"""
    assert len(y_true) == len(y_predict), \
        "the size of y_true must be equal to the size of y_predict"

    return np.sum(y_true == y_predict) / len(y_true)


def mean_squared_error(y_true, y_predict):
    """计算y_true和y_predict之间的MSE"""
    assert len(y_true) == len(y_predict), \
        "the size of y_true must be equal to the size of y_predict"

    return np.sum((y_true - y_predict)**2) / len(y_true)


def root_mean_squared_error(y_true, y_predict):
    """计算y_true和y_predict之间的RMSE"""

    return sqrt(mean_squared_error(y_true, y_predict))


def mean_absolute_error(y_true, y_predict):
    """计算y_true和y_predict之间的MAE"""
    assert len(y_true) == len(y_predict), \
        "the size of y_true must be equal to the size of y_predict"

    return np.sum(np.absolute(y_true - y_predict)) / len(y_true)


def r2_score(y_true, y_predict):
    """计算y_true和y_predict之间的R Square"""

    return 1 - mean_squared_error(y_true, y_predict)/np.var(y_true)

def TN(y_true, y_predict):
    assert len(y_true) == len(y_predict), \
    "The length of the y_true and y_predict must be equal!"
    true_negatives = np.array((y_true == 0) & (y_predict == 0), dtype='int')
    return np.sum(true_negatives)

def TP(y_true, y_predict):
    assert len(y_true) == len(y_predict), \
    "The length of the y_true and y_predict must be equal!"
    true_positives = np.array((y_true == 1) & (y_predict == 1), dtype='int')
    return np.sum(true_positives)

def FN(y_true, y_predict):
    assert len(y_true) == len(y_predict), \
    "The length of the y_true and y_predict must be equal!"
    false_negatives = np.array((y_true == 1) & (y_predict == 0), dtype='int')
    return np.sum(false_negatives)

def FP(y_true, y_predict):
    assert len(y_true) == len(y_predict), \
    "The length of the y_true and y_predict must be equal!"
    false_positives = np.array((y_true == 0) & (y_predict == 1), dtype='int')
    return np.sum(false_positives)


def confusion_matrix(y_true, y_predict):
    return np.array([
        [TN(y_true, y_predict), FP(y_true, y_predict)],
        [FN(y_true, y_predict), TP(y_true, y_predict)]
    ])

def Precision_Score(y_true, y_predict):
    assert len(y_true) == len(y_predict), \
        "The length of the y_true and y_predict must be equal!"
    tp = TP(y_true, y_predict)
    fp = FP(y_true, y_predict)
    try:
        return tp / (tp + fp)
    except:
        return 0.0
def Recall_Score(y_true, y_predict):
    assert len(y_true) == len(y_predict), \
    "The length of the y_true and y_predict must be equal!"
    tp = TP(y_true, y_predict)
    fn = FN(y_true, y_predict)
    try:
        return tp/(tp + fn)
    except:
        return 0.0

def F1_Score(y_true, y_predict):
    assert len(y_true) == len(y_predict), \
    "The length of the y_true and y_predict must be equal!"
    precision_score = Precision_Score(y_true, y_predict)
    recall_score = Recall_Score(y_true, y_predict)
    try:
        return 2/(1/precision_score + 1/recall_score)
    except:
        return 0.0

def TPR(y_true, y_predict):
    return Recall_Score(y_true, y_predict)

def FPR(y_true, y_predict):
    fp = FP(y_true, y_predict)
    tn = TN(y_true, y_predict)
    try:
        return fp/(fp + tn)
    except:
        return 0.0

