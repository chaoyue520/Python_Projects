# 加载库
import hashlib
import pandas as pd

data_set=pd.read_table('/data/home/jiwenchao/rh_phone_hash.txt',header=0,names=['phone'])

# 待加密信息
str_list = data_set['phone'].tolist()

md5_phone=[]
for strs in str_list:
	# 重新获取
    hl = hashlib.md5()
    strs = str(strs).encode('utf8')
    hl.update(strs)
    md5_phone.append(hl.hexdigest())


# 赋值并保持本地
data_set['md5_phone']=md5_phone
data_set[['phone','md5_phone']].to_csv('/data/home/jiwenchao/md5.txt',index=False)

