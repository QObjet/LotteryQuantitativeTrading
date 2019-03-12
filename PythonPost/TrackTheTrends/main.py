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
from PythonPost.Common.sum_progressive import *
import PythonPost.Common.spawn_data as sd
import PythonPost.TrackTheTrends.polyomial_manager as pm
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

slope_five_list=[]

# 使用虚拟数据
datas=sd.create_data(100)

# 使用真实数据
# data_frame=pd.read_csv('top_speed28.csv')
# datas=list(data_frame['number'])

# 计算SimpleSingleDouble
# ssd=SimpleSingleDouble()

# 计算SumProgressive
ssd=SumProgressive()

ssd.appends(datas)
x=np.arange(0,100,1)

# 计算SimpleSingleDouble
# y=ssd.sum_list_double

# 计算SumProgressive
y=ssd.sum_list

# plt.plot(x,y)
# fn=pm.keep_r_squared(x,y)
fn=pm.between_r_squared(x,y)
# plt.plot(x,fn(x))
# plt.show()

index=1

_fn=fn.deriv(m = 1)
slope_five=_fn(x[100-5:])
slope_five_list.append(slope_five)

while True:
    # plt.cla()

    data=sd.create_data()
    # data=datas[100+index-1:100+index]
    ssd.appends(data)
    x=np.arange(0,100+index,1)
    # y=ssd.sum_list_double
    y=ssd.sum_list

    # plt.plot(x,y)
    # fn=pm.keep_r_squared(x,y)
    fn=pm.between_r_squared(x,y)
    # plt.plot(x,fn(x))
    # plt.show()

    index+=1

    # 求导
    _fn=fn.deriv(m = 1)
    slope_five=_fn(x[100+index-6:])
    slope_five_list.append(slope_five)

    if index>960:
        break

slope_five_array=np.array(slope_five_list)

# 保存基本数据
dataframe = pd.DataFrame({'data':ssd.data,'post_list':ssd.post_list,'sum_list':ssd.sum_list})
dataframe.to_csv('PythonPost/TrackTheTrends/sum_single_double_data.csv',index=False,sep=',')

# 保存最近几次的斜率
dataframe = pd.DataFrame(slope_five_array, columns=['01', '02', '03', '04', '05']) 
dataframe.to_csv('PythonPost/TrackTheTrends/sum_single_double_result.csv',index=False,sep=',')

print('end')