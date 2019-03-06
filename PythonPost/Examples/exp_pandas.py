import pandas as pd

# pandas写入数据到*.csv
# 写入多列数据
dataframe = pd.DataFrame({'index':[1,2,3,4,5],
    'issue':[1024,1025,1026,1027,1028]})
dataframe.to_csv('PythonPost/Examples/exp_pandas_to_csv.csv',index=False,sep=',')

# pandas读取*.csv数据
datas=pd.read_csv('PythonPost/Examples/exp_pandas_to_csv.csv')
print(datas)