import pandas as pd 
import numpy as np 
import copy

data=pd.read_table('result_v1.txt',sep='\t',header=None,names=['dt','total_bid','fraud_cnt','credit_cnt','good_cnt','other_cnt'])
data_percent=copy.deepcopy(data)

n=data.shape[0]

for col in list(df.columns):
    for i in range(n):
        if col=='dt':
            data_percent['dt'][i]=data.iloc[i][0]
        else :
            # data_percent[col]=data_percent[col].astype(float)
            data_percent[col][i]=str(round(100.0*data[col][i]/data['total_bid'][i],2)) + '%'


data_percent.to_csv('result_v2.txt',sep='\t',header=False,index=False)