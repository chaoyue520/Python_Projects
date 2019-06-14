for col in col_x:
    ############################################################
    ##################分区间的情况
    
    if train_set[col].nunique()>= 10:
        train_set[col+"_bin"] = pd.qcut(train_set[col], q=10,duplicates='drop')
        a=pd.DataFrame(train_set.groupby([col+"_bin"]).size())
        c=[]
        for i in range(0,a.shape[0]):
            b=a.index[i].right
            c.append(b)
        m=a.index[0].left
        nn=list(set(np.append(m,c)))
        bin=sorted(list(set(np.append(m,c))))
        valid_set[col+"_bin"]= pd.cut(valid_set[col],bins=bin)
        
        ###计算psi
        b1=train_set.groupby([col+"_bin"])[col+"_bin"].agg(['count'])
        a1=valid_set.groupby([col+"_bin"])[col+"_bin"].agg(['count'])
        a1['qujian']=a1.index
        a1=a1.rename(index=str, columns={"count": "count_new"})
        a1['count_new_rate']=a1['count_new']/a1['count_new'].sum()
        b1['qujian']=b1.index
        b1['rate']=b1['count']/b1['count'].sum()
        c1=pd.merge(b1,a1,on='qujian',how='left')
        m1=0
        for i in c1.index:
            n1=(c1['count_new_rate'][i]-c1['rate'][i])*(math.log10(c1['count_new_rate'][i]/c1['rate'][i]))
            m1=m1+n1
        print(col+"_psi",'\t',m1)
        
    else:
    ############################################################
    ##################不需要分区间的情况（还有问题）
        b1=pd.DataFrame(train_set.groupby([col]).size())
        a1=pd.DataFrame(valid_set.groupby([col]).size())
        a1.columns=['count_new']
        b1.columns=['count']
        a1['qujian']=a1.index
        a1['count_new_rate']=a1['count_new']/a1['count_new'].sum()
        b1['qujian']=b1.index
        b1['rate']=b1['count']/b1['count'].sum()
        c1=pd.merge(b1,a1,on='qujian',how='left')
        m1=0
        for i in c1.index:
            n1=(c1['count_new_rate'][i]-c1['rate'][i])*(math.log10(c1['count_new_rate'][i]/c1['rate'][i]))
            if(pd.isnull(n1)==True):
                m1=m1
            else:
                m1=m1+n1
        print(col+"_psi",'\t',m1)