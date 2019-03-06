import numpy as np
import PythonPost.Common.ex_numpy_polyfit as exnp

step=2
curr_r_squared=0
first=True

def keep_r_squared(x,y):
    global step
    global curr_r_squared
    global first

    while True:
        if first:
            results=exnp.ex_polyfit(x,y,step)
            curr_r_squared=results['determination']
            fn=np.poly1d(results['polynomial'])
            if curr_r_squared>=0.9:
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