# python

enumerate(): 
是一个 Python 内置函数，用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
range() 生成一个整数列表，用在for循环中。 

enumerate()函数会返回一个包含元组的列表，元组中第一个元素是索引，第二个元素是原来列表的元素，在for循环中遍历很方便。 
```python
cities = ['HZ', 'XA', 'BJ', 'NY', 'NJ']
for i, city in enumerate(cities):
    print(i, city)
```
结果:

```python
0 HZ
1 XA
2 BJ
3 NY
4 NJ
```

```python
        def dJ(theta, X_b, y):
            gd = np.zeros_like(theta)
            for i in range(len(theta)):
                if i == 0:
                    gd[0] = np.sum((X_b.dot(theta) - y))
                else:
                    gd[i] = np.sum((X_b.dot(theta) - y).dot(X_b[:, i]))
            return gd * 2 / len(X_b)
```