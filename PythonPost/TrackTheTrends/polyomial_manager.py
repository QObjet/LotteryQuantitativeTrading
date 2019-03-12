import numpy as np
import PythonPost.Common.ex_numpy_polyfit as exnp

'''
多项式拟合次数不能超过19
'''

step=2
curr_r_squared=0
first=True

cut_index=0

def keep_r_squared(x,y):
    '''
    squared这一次比上一次少：增加阶数
    '''
    global step
    global curr_r_squared
    global first

    while True:
        if first:
            results=exnp.ex_polyfit(x,y[0:],step)
            curr_r_squared=results['determination']
            fn=np.poly1d(results['polynomial'])
            if curr_r_squared>=0.85:
                print('First step:%d squared:%f'%(step,curr_r_squared))
                first=False
                return fn
            step+=1
        else:
            results=exnp.ex_polyfit(x,y[0:],step)
            r_squared=results['determination']
            fn=np.poly1d(results['polynomial'])
            if r_squared>=curr_r_squared:
                curr_r_squared=r_squared
                print('First step:%d squared:%f'%(step,curr_r_squared))
                return fn
            else:
                step+=1
                results=exnp.ex_polyfit(x,y[0:],step)
                r_squared=results['determination']
                fn=np.poly1d(results['polynomial'])
                curr_r_squared=r_squared
                print('First step:%d squared:%f'%(step,curr_r_squared))
                return fn

def between_r_squared(x,y):
    '''
    squared在两个数之间：少增加阶数 多减少阶数
    '''
    global step
    global curr_r_squared
    global first
    global cut_index

    index=0
    
    while True:
        index+=1
        if first:
            results=exnp.ex_polyfit(x,y[0:],step)
            curr_r_squared=results['determination']
            fn=np.poly1d(results['polynomial'])
            if curr_r_squared>=0.80:
                # print('First step:%d squared:%f'%(step,curr_r_squared))
                first=False
                return fn
            step+=1
        else:
            results=exnp.ex_polyfit(x,y[0:],step)
            r_squared=results['determination']
            fn=np.poly1d(results['polynomial'])
            if r_squared>=0.75 and r_squared<=0.85:
                curr_r_squared=r_squared
                # print('First step:%d squared:%f'%(step,curr_r_squared))
                return fn
            elif r_squared<0.85:
                step+=1
                if step>18:
                    step=2
                    cut_index+=(len(y)-cut_index)/2
                    index=0
                if index>100:
                    return fn
            elif step>2:
                step-=1
                if index>10:
                    return fn
            else:
                return fn