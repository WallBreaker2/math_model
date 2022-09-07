from turtle import color
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
# matplotlib其实是不支持显示中文的 显示中文需要一行代码设置字体
mpl.rcParams['font.family'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False   # 步骤二（解决坐标轴负数的负号显示问题
# 1.基本绘图
# 创建画板1
fig = plt.figure(1)

# --- 设置坐标轴位置 ----
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
# ---- end ----

x = np.arange(0,5,0.2)
y = np.sin(x)
y1 = x
y2 = x - np.power(x, 3) / 6.0
y3 = x - np.power(x, 3) / 6.0 + np.power(x, 5) / 120.0
plt.plot(x, y, color='r', marker='o', linestyle='--', label=r'$\sin(x)$')
plt.plot(x, y1, color='b', marker='x', linestyle='-', label = r'$x$')
plt.plot(x, y2, color='k', marker='v', linestyle='-.', label = r'$x-\frac{x^3}{6}$')
plt.plot(x, y3, color='g', linestyle='-', label = r'$x-\frac{x^3}{6}+\frac{x^5}{120}$')

# 坐标轴范围
plt.axis([0,5,-2,2])
# 图例
plt.legend(loc='lower left')
# 坐标轴文本
plt.xlabel('x轴')
plt.ylabel('y轴')
# 标题
plt.title(r'$\sin(x)$的泰勒展开')
# 注释
plt.annotate(r'$x-\frac{x^3}{6}$', xy=(3,-1.5), 
            xytext=(4,-1.5),arrowprops=dict(arrowstyle='->', facecolor='blue'))

# --------------- 子图 -------------------
# 创建画板2
fig2 = plt.figure(2)
# 创建画纸并使用画纸1
ax1 = plt.subplot(2,1,1)
plt.plot(x,y)
# 创建画纸并使用画纸2
ax2 = plt.subplot(2,1,2)
plt.plot(x,y3)

plt.show()
# -------------- 散点图 ------------
x = np.random.normal(0, 1, 100)
y = np.random.normal(0, 1, 100)
import pylab
pylab.figure(1)
pylab.scatter(x,y)

# 等高线
pylab.figure(2)
def f(x,y): return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)

n = 256
x = np.linspace(-3,3,n)
y = np.linspace(-3,3,n)
X,Y = np.meshgrid(x,y)

pylab.contourf(X, Y, f(X,Y), 8, alpha=.75, cmap='jet')
C = pylab.contour(X, Y, f(X,Y), 8, colors='black', linewidth=.5)


pylab.show()


