#!/usr/bin/python
# encoding=UTF-8


# 极端值分布
def outlier_check(df,c_name):
    p=df[[c_name]].boxplot(return_type='dict')
    x_outliers=p['fliers'][0].get_xdata()
    y_outliers = p['fliers'][0].get_ydata()
    for j in range(1):
        plt.annotate(y_outliers[j], xy=(x_outliers[j], y_outliers[j]), xytext=(x_outliers[j] + 0.02, y_outliers[j]))
    plt.show()




# 判断data_set数据集, columns_v1字段的极端值分布
outlier_check(data_set,'column_v1')