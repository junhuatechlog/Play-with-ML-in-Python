# Scikit-learn

# 变量

如果在一个类中拟合后生成了新的变量用来存储拟合结果， 比如参数学习里面的参数，则新生成的参数名后面加下划线 "_": 为了便于区分，自己设计的类中生成的变量的变量名前面加上下划线 "_".
```python
        self.coef_ = self._theta[1:]
        self.intercept_ = self._theta[0]
```