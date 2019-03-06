import matplotlib.pyplot as plt
import numpy as np

# Polynomial Regression
def ex_polyfit(x, y, degree):
    '''
    numpy多项式拟合
    扩展添加计算r-squared
    多项式参数:results['polynomial']
    r-squared:results['determination']
    '''
    results = {}

    coeffs = np.polyfit(x, y, degree)

    # Polynomial Coefficients
    results['polynomial'] = coeffs.tolist()

    # r-squared
    p = np.poly1d(coeffs)
    # fit values, and mean
    yhat = p(x)                      # or [p(z) for z in x]
    ybar = np.sum(y)/len(y)          # or sum(y)/len(y)
    ssreg = np.sum((yhat-ybar)**2)   # or sum([ (yihat - ybar)**2 for yihat in yhat])
    sstot = np.sum((y - ybar)**2)    # or sum([ (yi - ybar)**2 for yi in y])
    results['determination'] = ssreg / sstot

    return results

# 创建等差数列
x = list(np.arange(0,10,0.1))
# 给2次多项式添加噪音
y = list(map(lambda val: val**2*3 + val*3 + np.random.random()*100 , x) )

# 绘制散点图
plt.scatter(x, y)

#指明用3次多项式匹配
w = ex_polyfit (x, y, 3)  # 最小二乘法
fn = np.poly1d(w['polynomial'])

#打印适配出来的参数和函数
print(w)
print(fn)

# 画图
plt.plot(x, fn(x))
plt.show()