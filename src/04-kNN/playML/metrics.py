import numpy as np

def accuracy_score(y_true, y_predict):
    assert y_true.shape[0] == y_predict.shape[0], \
    "the size of y_true and y_predict should be equal!"
    return sum(y_true == y_predict)/len(y_true)