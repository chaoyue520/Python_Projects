#!/usr/bin/python
# -*- coding: UTF-8 -*-

from sklearn.cross_validation import train_test_split

# 原始样本先拆分为X和y
X=data_set_v2.drop(['d7_mob2'],axis=1)
y=data_set_v2['d7_mob2']


# step 1 : 先区分oot sample
X_train_1, X_oot, y_train_1, y_oot = train_test_split(X, y, test_size=0.15, random_state=42)

# oot sample
oot_set=pd.concat([X_oot,y_oot],axis=1)
oot_set.head()


# step 2 : 再拆分Train Test
X_train, X_test, y_train, y_test = train_test_split(X_train_1, y_train_1, test_size=0.25, random_state=42)

# 合并数据集生成 train sample
train_set=pd.concat([X_train,y_train],axis=1)
train_set.head()

# 合并数据集生成 valid sample
valid_set=pd.concat([X_test,y_test],axis=1)
valid_set.head()



