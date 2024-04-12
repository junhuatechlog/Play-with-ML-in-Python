


### Jupyter notebook修改默认工作路径
在powershell下用jupyter notebook --generate-config生成配置文件: .jupyter/jupyter_notebook_config.py
Jupyter notebook 使用安装路径作为默认路径，如果要修改默认路径，需要修改.jupyter/jupyter_notebook_config.py里的 c.ServerApp.root_dir
设置这个路径时，为了避免将字符串里路径的反斜杠解释为转义字符，有2种方法：
1. 在反斜杠前面另加一个反斜杠，将其转义
2. 使用原始字符串(raw string)的特性 - 在字符串前面加r.
c.ServerApp.root_dir = r'C:\N-20KEPC0Y7KFA-Data\junhuawa\Documents\Play-with-ML-in-Python\src\04-kNN'



import sys
sys.path.append('C:\Users\junhuawa\PycharmProjects\playML')

### 打开其他文件夹下的jpynb文件
在powershell prompt下，输入给jupyter notebook输入对应的目录

jupyter notebook C:\N-20KEPC0Y7KFA-Data\junhuawa\Documents\Play-with-ML-in-Python\src\Basics


### python interpretor path

C:\Users\junhuawa\AppData\Local\anaconda3\python.exe

Settings/Project/Python Interpreter