#!/usr/bin/python
# -*- coding: utf-8 -*-


import pandas as pd
import numpy as np
import sys
import time

# parameter
clf_freq_n = 3


def var_stat(data, clf_freq_n, output_file):
	# --------------------------------------------------------------------------------------
	# continuous var: output miss_rate, zero_rate, mean, std, min, p01, p25, p50, p75,
	# 					     p99, max, is_all_null, is_unique_val, is_all_null_or_uniq
	# discrete   var: output miss_rate, cnt_dist_values, freq_top_n, freq_bottom_n
	# --------------------------------------------------------------------------------------
	
	n_row = float(data.shape[0])
	n_col = data.shape[1]
	stat_num = []
	stat_clf = []

	for i in range(n_col):
		var = data[data.columns[i]]
		var_nonan = var[var.notnull()]
		name = data.columns[i]

		# continuous var stat
		if ('int' in str(var.dtype)) or ('float' in str(var.dtype)):
			miss_rate = pd.isnull(var).sum()/n_row 
			zero_rate = var.eq(0).sum()/n_row
			mean = var_nonan.mean()
			std = var_nonan.std()
			min = var_nonan.min()
			p01 = var_nonan.quantile(.01)
			p25 = var_nonan.quantile(.25)
			p50 = var_nonan.quantile(.5)
			p75 = var_nonan.quantile(.75)
			p99 = var_nonan.quantile(.99)
			max = var_nonan.max()
			if miss_rate == 1: is_all_null = 1 
			else: is_all_null = 0
			if min == max: is_unique_val = 1 
			else: is_unique_val = 0
			is_all_null_or_uniq = is_all_null | is_unique_val
			stat_num.append(np.array([name, miss_rate, zero_rate, mean, std, min, p01, p25, \
									   p50, p75, p99, max, is_all_null, is_unique_val, is_all_null_or_uniq], np.str))
		
		# discrete var stat
		else:
			miss_rate = pd.isnull(var).sum()/n_row
			cnt_dist_values = len(var_nonan.drop_duplicates())
			val_freq = data.groupby(data.columns[i]).size().sort_values(ascending = False)
			n_val = len(val_freq)
			freq_top_n = ''
			freq_bottom_n = ''
			for i in range(clf_freq_n):
				if n_val > i:
					freq_top_n += str(val_freq.index[i]) + ' : ' + str(round(val_freq[i] / n_row, 4)*100) + '%; '
					freq_bottom_n += str(val_freq.index[-(i+1)]) + ' : ' + str(round(val_freq[-(i+1)] / n_row, 4)*100) + '%; '
				else: break
			stat_clf.append(np.array([name, miss_rate, cnt_dist_values, freq_top_n, freq_bottom_n], np.str))
			
	head_cont = ['name', 'miss_rate', 'zero_rate', 'mean', 'std', 'min', 'p01', 'p25', 'p50', 'p75', 'p99', 'max', 'is_all_null', 'is_unique_val', 'is_all_null_or_uniq']
	head_disc = ['name', 'miss_rate', 'cnt_dist_values', 'freq_top_n', 'freq_bottom_n']
	
	with open(output_file, 'wt') as f:
		f.write('Record count: ' + str(int(n_row)) + '\n')
		f.write('Var count: ' + str(n_col) + '\n')
		f.write('\n\nNumeric var stat\n')
		f.write('\t'.join(head_cont) + '\n')
		for i in range(len(stat_num)):
			f.write('\t'.join(stat_num[i]) + '\n')
		
		f.write('\n\nClassify var stat\n')
		f.write('\t'.join(head_disc) + '\n')
		for i in range(len(stat_clf)):
			f.write('\t'.join(stat_clf[i]) + '\n')

	
if __name__ == '__main__':
	print("\nLet's go.\n")
	start_time = time.clock()
	
	# read var names
	print('Read var names ...')
	var_names_type = pd.read_table(sys.argv[1],
							   	   sep = '\t',
							       header = None)
	var_names = np.array(var_names_type[var_names_type.columns[0]])
	
	# read data
	print('Read data ...')
	data = pd.read_table(sys.argv[2],
						 sep = '\t',
						 header = None,
						 names = var_names,
						 na_values = ['NA', 'na', 'NULL', 'null', ''])

	end_time_1 = time.clock()
	print('  time consumed: %d s' % int(end_time_1 - start_time)) 
	
	# var stat 
	print('\nVar stat ...')
	var_stat(data, clf_freq_n, sys.argv[3])

	end_time = time.clock()
	print('  time consumed: %d s' % int(end_time - end_time_1))

	print('\nDone. ^_^')

	end_time = time.clock()
	print('Total time consumed: %d s' % int(end_time - start_time))

