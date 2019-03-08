import numpy as np
import PythonPost.Common.ex_numpy_polyfit as exnp



step=2
curr_r_squared=0
first=True

def keep_r_squared(x,y):
    '''
    squared这一次比上一次少：增加阶数
    '''
    global step
    global curr_r_squared
    global first

    while True:
        if first:
            results=exnp.ex_polyfit(x,y,step)
            curr_r_squared=results['determination']
            fn=np.poly1d(results['polynomial'])
            if curr_r_squared>=0.85:
                print('First step:%d squared:%f'%(step,curr_r_squared))
                first=False
                return fn
            step+=1
        else:
            results=exnp.ex_polyfit(x,y,step)
            r_squared=results['determination']
            fn=np.poly1d(results['polynomial'])
            if r_squared>=curr_r_squared:
                curr_r_squared=r_squared
                print('First step:%d squared:%f'%(step,curr_r_squared))
                return fn
            else:
                step+=1
                results=exnp.ex_polyfit(x,y,step)
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

    index=0
    
    while True:
        index+=1
        if first:
            results=exnp.ex_polyfit(x,y,step)
            curr_r_squared=results['determination']
            fn=np.poly1d(results['polynomial'])
            if curr_r_squared>=0.90:
                # print('First step:%d squared:%f'%(step,curr_r_squared))
                first=False
                return fn
            step+=1
        else:
            results=exnp.ex_polyfit(x,y,step)
            r_squared=results['determination']
            fn=np.poly1d(results['polynomial'])
            if r_squared>=0.90 and r_squared<=0.92:
                curr_r_squared=r_squared
                # print('First step:%d squared:%f'%(step,curr_r_squared))
                return fn
            elif r_squared<0.95:
                step+=1
                if index>100:
                    return fn
            elif step>2:
                step-=1
                if index>10:
                    return fn
            else:
                return fn