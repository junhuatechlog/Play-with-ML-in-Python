# Numpy functions

```python
import numpy as np
x = np.linspace(-1, 6, 141)
numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)[sourc
```
返回一个一维数组，默认返回的是一个包含endpoint的闭区间，如果不想包含endpoint，则endpoint=False.



对一个列表里的值做相同的操作

```python
def J(theta):
    return (theta-2.5)**2 - 1
theta_history=[1, 2, 3, 4, 5, 6]
theta_y = [J(i) for i in theta_history]
```
用numpy array方式:
``` python
theta_history=[1, 2, 3, 4, 5, 6]
theta_y = J(np.array(theta_history))
```


从一个数组中选出满足条件的点：

```python
test_list = np.array([3, 2, 1, 4, 7, 2, 3, 4, 9, 8])
index = np.array((test_list >= 3) & (test_list <= 7))#从中选出>=3, <=7的点
test_list[index]
```
结果：

`array([3, 4, 7, 3, 4])`