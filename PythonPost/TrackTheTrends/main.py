if __name__=='__main__':
    import sys
    import os
    # 获取当前绝对路径
    curPath = os.path.abspath(os.path.dirname(__file__))
    rootPath = os.path.split(curPath)[0]
    rootPath = os.path.split(rootPath)[0]
    print(rootPath)
    # 设置模块搜索路径为Root目录
    sys.path.append(rootPath)

from PythonPost.Common.simple_single_double import *
import PythonPost.Common.spawn_data as sd
import PythonPost.TrackTheTrends.polyomial_manager as pm
import numpy as np
import matplotlib.pyplot as plt

datas=sd.create_data(100)
ssd=SimpleSingleDouble()
ssd.appends(datas)
x=np.arange(0,100,1)
y=ssd.sum_list_double

plt.scatter(x,y)
fn=pm.keep_r_squared(x,y)
plt.plot(x,fn(x))
plt.show()

index=5

while True:
    plt.cla()

    data=sd.create_data(5)
    ssd.appends(data)
    x=np.arange(0,100+index,1)
    y=ssd.sum_list_double

    plt.scatter(x,y)
    fn=pm.keep_r_squared(x,y)
    plt.plot(x,fn(x))
    plt.show()
    index+=5
