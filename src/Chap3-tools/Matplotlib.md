# Matplotlib 学习笔记

Matplotlib是Numpy的附加组件，输出Matlab质量的图形。 使用类的面向对象的方式。
图形 (Figure) 类实例等同于艺术家称为 "画布" 的东西。一个图形中可能有一个或者多个轴 (Axes)类的实例。轴 (Axes)代表坐标轴 (一个X轴和一个y轴) 的集合！  
在使用中，如果直接调用 plt.plot() 绘图，则会默认创建一个图形类和一个轴.

### 下面两段代码生成同一个图形:
```python
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-np.pi, np.pi, 101)
y = np.sin(x)+np.sin(3*x)/3.0
fig = plt.figure()
ax = fig.add_subplot(121)
ax.plot(x, y)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('A simple plot')
```
```python
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-np.pi, np.pi, 101)
y = np.sin(x)+np.sin(3*x)/3.0
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('A simple plot')
```
![一个简单图形示例](images/matplotlib/simple.png)

### 在一个图形中绘制多个坐标轴

```python
x = np.linspace(0, 5, 101)
y1 = 1.0/(x+1.0)
y2 = np.exp(-x)
y3 = np.exp(-0.1*x**2)
y4 = np.exp(-5*x**2)

fig = plt.figure() # 构造一个图形类对象
ax1 = fig.add_subplot(221) #构造一个轴子图类对象
ax1.plot(x, y1)
ax1.set_xlabel('x')
ax1.set_ylabel('y1')
ax1.set_title('A simple plot')#设置子图的标题
ax2 = fig.add_subplot(222)#参数也可以写成 (2, 2, 2)
ax2.plot(x, y2)
ax2.set_xlabel('x')
ax2.set_ylabel('y2')
ax2.set_title('A simple plot')
ax3 = fig.add_subplot(223)
ax3.plot(x, y3)
ax3.set_xlabel('x')
ax3.set_ylabel('y3')
ax3.set_title('A simple plot')
ax4 = fig.add_subplot(224)
ax4.plot(x, y4)
ax4.set_xlabel('x')
ax4.set_ylabel('y4')
ax4.set_title('A simple plot')
fig.tight_layout()
fig.suptitle('Various decay functions') #绘制标题
```
![在一个图形中绘制多个坐标轴](images/matplotlib/4axes.png)

### 绘制等高线 
也称水平线，是一种在二维平面显示3D图像的方法

```python
import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
[X, Y]=np.mgrid[-2.5:2.5:51j, -3:3:61j]
Z=X**2+Y**2
curves = ax.contour(X,Y,Z,12,colors='k')
ax.clabel(curves)
fig.suptitle(r'The level contours of $z=x^2+y^2$', fontsize=20)
```
![绘制等高线](images/matplotlib/contour.png)

### 绘制带颜色的等高曲线图

```python
import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
[X, Y]=np.mgrid[-2.5:2.5:51j, -3:3:61j]
Z=X**2+Y**2
curves = ax.contour(X, Y, Z, 12)#用contourf可以得到颜色填充的等高曲线图
ax.clabel(curves)
fig.suptitle(r'The level contours of $z=x^2+y^2$', fontsize=20)
fig.colorbar(curves, orientation='vertical')
```
![带颜色的等高曲线图](images/matplotlib/color.png)

### 绘制柱状图
给他一个数列，他会对数列里各个值的数量做统计，然后用柱状图表示出来。 
Compute and plot a histogram.

```python
x = np.random.normal(0, 1, 100)# 创建一个均值为0， 标准差为1 的100个数的数列
plt.hist(x)
```
返回：
返回两个数组，第一个数组列出数列中每个值对应的个数 - counts；
第二个数组列出桶的列表 - bins。
```python
(array([ 1.,  5.,  7., 13., 17., 18., 16., 11.,  7.,  5.]),
 array([-2.55298982, -2.07071537, -1.58844093, -1.10616648, -0.62389204,
        -0.1416176 ,  0.34065685,  0.82293129,  1.30520574,  1.78748018,
         2.26975462]),
 <BarContainer object of 10 artists>)

```
![](images/matplotlib/hist.jpg)

### 画出正态分布的概率密度函数和柱状图

```python
x = np.random.normal(0, 1, 1000)
x = np.sort(x)
def gaussian(mu, sigma, x):
    return 1/(np.sqrt(2*np.pi) * sigma) * np.exp(-(x - mu)**2/(2*sigma**2))

y = gaussian(0, 1, x)
plt.hist(x, density=True, bins='auto') #density 表示返回的是概率密度值，也可以指定桶的数量
plt.plot(x, y)

```
概率密度值 = each bin will display the bin's raw count divided by the total number of counts *and the bin width*

这里的bin是桶的意思。 
scipy.stats.norm.pdf() - Probability density function 
![](images/matplotlib/hist-pd.jpg)