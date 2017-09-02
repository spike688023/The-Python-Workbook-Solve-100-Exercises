#Plot the data in the file provided through the URL http://www.pythonhow.com/data/sampledata.txt
import pandas
import pylab as plt

data = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
data.plot(x='x', y='y', kind='scatter')
plt.show()

"""
這是另種 作法。
from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas

output_file("bokeh_plot.html")
data = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
f = figure()
f.circle(x=data["x"], y=data["y"])

show(f)
"""



"""
下面都是我的東西。
"""
Simple demo of a scatter plot.
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas

data = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
N = len(data.x.values)

#x = np.random.rand(N)
#y = np.random.rand(N)
x = np.array(data.x.values)
y = np.array(data.y.values)
colors = np.random.rand(N)
area = np.pi * (15 * np.random.rand(N))**2  # 0 to 15 point radii

plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()

這種 help很難看的， 只能到官網 求幫助了。

直接看官網 比較 快， 下面的連結，會把  畫出來的樣式，列出來，

你可以選一個，自已覺得 最符合的來用。
https://matplotlib.org/gallery.html#lines_bars_and_markers
"""


"""
這裡又會一個東西了， 概然我知道x 是個numpy.ndarray的 物件，

我就 可以去看，怎麼建立一個ndarray的物件， 用help() function後，

還要再去找Example 來看，是最方便的。
>>> x = np.random.rand(2)
>>> type(x)
<class 'numpy.ndarray'>

|  Examples
|  --------
|  Manually adding two vectors, using broadcasting:
|
|  >>> x = np.array([[1], [2], [3]])
|  >>> y = np.array([4, 5, 6])
"""
