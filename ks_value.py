#!/bin/python
# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np
import os

os.getcwd()

na_values = ['', 'NA', 'na', 'NULL', 'null', 'NaN', 'nan', '\\N']

def get_lift(data_file, n_groups, output_file, y_name='y', score_name='score') :
    
    '''
    data_file: 要带表头，\t分割
    '''
    # load data
    data = pd.read_table(data_file, na_values = na_values)
    # sort by score
    data_sorted = data.sort_values(by = score_name, axis = 0, ascending = False)
    # group and stat
    n_rcds = data_sorted.shape[0]
    n_rcd_p_group = int(float(n_rcds)/n_groups)
    n_fraud_all = data_sorted[y_name].sum()	# 总欺诈数
    stat = []
    for i in range(n_groups):
        y_this_g = pd.Series(np.array(data_sorted[y_name])[i*n_rcd_p_group : (i+1)*n_rcd_p_group])
        score_this_g = pd.Series(np.array(data_sorted[score_name])[i*n_rcd_p_group : (i+1)*n_rcd_p_group])
        id = i+1
        # 分组模型平均分
        avg_score_g = score_this_g.dropna().mean()
        # 分组欺诈数
        n_fraud_g = y_this_g.dropna().sum()
        # 分组欺诈率
        r_fraud_g = float(n_fraud_g) / n_rcd_p_group
        # 每组的最后一个分数
        last_score_g = score_this_g.dropna().min()
        #实际好
        n_real_good = n_rcd_p_group - n_fraud_g
        #实际坏
        n_real_bad = n_fraud_g
        # 分组累计
        y_total_g = pd.Series(np.array(data_sorted[y_name])[0 : (i+1)*n_rcd_p_group])
        #累计好
        n_total_good = y_total_g.dropna().count() - y_total_g.dropna().sum()
        #累计坏
        n_total_bad = y_total_g.dropna().sum()
        #累计好占比
        r_total_good_ratio = float(n_total_good) / n_rcds
        #累计坏占比  等价于 累计捕获率
        r_total_bad_ratio = float(n_total_bad) / n_fraud_all
        # ks
        n_ks_value = r_total_bad_ratio - r_total_good_ratio


        # append每行数据存在list中
        stat.append([id, n_fraud_all, n_rcd_p_group, avg_score_g, n_fraud_g, r_fraud_g, last_score_g, \
                     n_real_good,n_real_bad,n_total_good,n_total_bad,r_total_good_ratio,r_total_bad_ratio,n_ks_value])

    # 累计捕获率 等价于 累计坏占比
    r_capture_acc = []
    acc = 0
    n = len(stat)
    for i in range(n):
        acc += float(stat[i][4])/stat[i][1]
        r_capture_acc.append(acc)

    # output lift result
    header = ['分组', '总欺诈数', '分组交易数', '分组模型平均分', '分组欺诈数', '分组欺诈率', '分组最小得分', \
              '实际好','实际坏','累计好','累计坏','累计好占比','累计坏占比','ks_value','累计捕获率']

    n_col = len(stat[0])
    with open(output_file, 'wt') as f:
        f.write('\t'.join(header) + '\n')
        for i in range(len(stat)):
            for j in range(n_col):
                f.write(str(stat[i][j]) + '\t')
            f.write(str(r_capture_acc[i]) + '\n')


'''
注意：output file 中 累计坏占比 与 累计捕获率 一样，只是名称不同罢了，两种不同的计算方法

'''

if __name__ == '__main__':
    data_file = '/home/fsg/jiwenchao/zx_score_card/zx_special_data_set_score.txt'
    y_name='m2_tag'
    score_name='score'
    n_groups = 1000
    output_file = '/home/fsg/jiwenchao/zx_score_card/v1.txt'
    get_lift(data_file, n_groups, output_file, y_name, score_name)




