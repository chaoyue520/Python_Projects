#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
import json
reload(sys)
sys.setdefaultencoding('utf8')
import commands
import time
import os
import datetime
import pandas as pd
import numpy as np
import traceback 
import urllib2
import urllib
import pymysql.cursors

os.system('LANG="zh_CN.UTF-8"')

# 定义发送数据格式和结构
def send_hi(filename):
    content=pd.read_table(filename
              ,header=None
              ,names=['risk_time','rim_dt','event_hashcode','trans_id','user_id','sp_id','business_type'\
                      ,'goods_name','grouptype','payamount','scrap_amount','confirm_amount','eventtype']
              ,encoding='utf-8'
              ,sep='\t')
    #分别求出笔数，人数，和金额    
    cnt_transId=content.groupby(['grouptype'])['trans_id'].count()
    dis_cnt_uid=content[['grouptype','user_id']].drop_duplicates().groupby(['grouptype'])['user_id'].count()
    sum_confirm_amt=pd.pivot_table(content,index=["grouptype"],values=['confirm_amount'],aggfunc={'confirm_amount':np.sum})
    send_data=pd.concat([cnt_transId,dis_cnt_uid,sum_confirm_amt],axis=1)
    #重命名
    send_data=send_data.rename_axis({'trans_id': u'cnt', 'user_id': u'dist_uid','confirm_amount': u'sum_payamt'}, axis='columns')
    # 设置发送格式
    data = {}
    data['msg'] = send_data
	data['to_group'] = 'xxxxxx'
	data['instance'] = 'robot_03'
	url = 'xxxxxxxxxxxxxxxxxxx'
    post_data = urllib.urlencode(data)
    req = urllib2.urlopen(url, post_data)
    return None


def logerror(title='title'):
    traceback.print_exc()
    with open('error.txt','a') as file:
        file.write('----------'+str(datetime.datetime.now())+'\n'+title+'\n'+str(traceback.format_exc())+'\n')


def send_myself(filename):
	with open(filename,'r') as file:
		content=file.read()
	data = {}
	data['msg'] = content
	data['to_group'] = 'xxxxxx'
	data['instance'] = 'robot_03'
	url = 'xxxxxxxxxxxxxxxxxxx'
	post_data = urllib.urlencode(data)
	req = urllib2.urlopen(url, post_data)
	return None


def sendhi(filename):
	content=filename
	data = {}
	data['msg'] = content
	data['to_group'] = 'xxxxxx'
	data['instance'] = 'robot_03'
	url = 'xxxxxxxxxxxxxxxxxxx'
	post_data = urllib.urlencode(data)
	req = urllib2.urlopen(url, post_data)
	return None



# 周一发近三天的，其他工作日发前一天的
# 周一发近三天的，其他工作日发前一天的
try:
    if int(time.strftime("%w")) == 1:
        filename=str('./daily_data_')+datetime.datetime.strftime(datetime.datetime.now() - datetime.timedelta(days=3),'%Y_%m_%d')+str('.txt')
        a=os.popen(str('wc -l ')+filename).readlines()[0].split( )[0]
        if int(a) == 0 : 
            sendhi('昨日无报损')
        else : 
            send_hi(filename)
            sendhi('近三天报损，请相关负责人查看')
            print(str('星期')+str(int(time.strftime("%w")))+str(':task success!'))
    elif int(time.strftime("%w")) in (2,3,4,5):
        filename=str('./daily_data_')+datetime.datetime.strftime(datetime.datetime.now() - datetime.timedelta(days=1),'%Y_%m_%d')+str('.txt')
        a=os.popen(str('wc -l ')+filename).readlines()[0].split( )[0]
        if int(a) == 0 : 
            sendhi('昨日无报损')
        else : 
            send_hi(filename)
            sendhi('昨天报损，请相关负责人查看')
            print(str('星期')+str(int(time.strftime("%w")))+str(':task success!'))     
except IOError as e:
    print e.message
    sendhi('hive罢工了，赶紧上GP跑报损数据了')

