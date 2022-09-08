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


# -------------- 散点图 ------------
# plt.style.use('_mpl-gallery')

# make the data
np.random.seed(3)
x = 4 + np.random.normal(0, 2, 24)
y = 4 + np.random.normal(0, 2, len(x))
# size and color:
sizes = np.random.uniform(15, 80, len(x))
colors = np.random.uniform(15, 80, len(x))

fig3 =plt.figure(3)
# 创建画纸并使用画纸1
ax = plt.subplot(2,3,1)

ax.scatter(x, y, s=sizes, c=colors, vmin=0, vmax=100)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))
# 条形图
x = 0.5 + np.arange(8)
y = np.random.uniform(2, 7, len(x))
# 创建画纸并使用画纸2
ax = plt.subplot(2,3,2)
plt.bar(x, y, width=1, edgecolor="white", linewidth=0.7)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))
ax.set_title('条形图')
# 茎图
ax = plt.subplot(2,3,3)

ax.stem(x, y)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))
ax.set_title('茎图')
# 阶梯图
ax = plt.subplot(2,3,4)

ax.step(x, y, linewidth=2.5)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))
ax.set_title('阶梯图')
# 填充图
np.random.seed(1)
x = np.linspace(0, 8, 16)
y1 = 3 + 4*x/8 + np.random.uniform(0.0, 0.5, len(x))
y2 = 1 + 2*x/8 + np.random.uniform(0.0, 0.5, len(x))

# plot
ax = plt.subplot(2,3,5)

ax.fill_between(x, y1, y2, alpha=.5, linewidth=0)
ax.plot(x, (y1 + y2)/2, linewidth=2)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))
ax.set_title('填充图')
# 扇形图
# make data
x = [1, 2, 3, 4]
colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(x)))

# plot
ax = plt.subplot(2,3,6)
ax.pie(x, colors=colors, radius=3, center=(4, 4),
       wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))
ax.set_title('扇形图')

# 流
# plot:
plt.figure(4)
ax = plt.subplot(2,1,1)
plt.style.use('_mpl-gallery-nogrid')

# make a stream function:
X, Y = np.meshgrid(np.linspace(-3, 3, 256), np.linspace(-3, 3, 256))
Z = (1 - X/2 + X**5 + Y**3) * np.exp(-X**2 - Y**2)
# make U and V out of the streamfunction:
V = np.diff(Z[1:, :], axis=1)
U = -np.diff(Z[:, 1:], axis=0)



ax.streamplot(X[1:, 1:], Y[1:, 1:], U, V)


plt.show()


