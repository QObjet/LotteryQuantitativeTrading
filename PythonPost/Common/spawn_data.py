import numpy as np

'''
根据28游戏规则创建数据
原始数据0-9 *3
开奖数据求和 范围0-27
'''

def create_origin_data(row=1):
    '''
    原始数据
    row 数据行数
    '''

    return np.random.randint(low=0,high=10,size=(row,3))

def create_data(row=1):
    '''
    开奖数据
    row 数据行数
    '''
    
    origin_data_list=create_origin_data(row)
    data_list=[]
    
    for temp in origin_data_list:
        data_list.append(np.sum(temp))
        
    return data_list