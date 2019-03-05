import os, sys
import numpy as np
import pandas as pd

class rawseries:
	def __init__(self, datapath):
		## Open .dat file
		id = open(datapath)
		lines = id.readlines()
		keys = ['exptime', 'shdalt', 'igeo', 'timeobs', 'zdbin','cent',
				'dopw','percent_cas','gallon','vlsr','slope']
		d = []
		i = 0
		for line in lines:
			i = i + 1
			if i==1:
				first = line.split()
			if i==2:
				second = line.split()
				dpt = [float(x) for x in first+second]
				d.append(dpt)
				i=0
		data = np.array(d)
		self.df = pd.DataFrame(data,columns=keys)

def sortby(df, by):
	keys = ['exptime', 'shdalt', 'igeo', 'timeobs', 'zdbin','cent',
				'dopw','percent_cas','gallon','vlsr','slope']

	if by in keys:
		return df.sort_values(by=by)
	else:
		print('Warning: sortby value does not exist')
		return df
			
def splitby(df, by, **args):
	# Options are 'zdbin' or 'AM/PM'
	time = args.get('time',6)
	if by=='zdbin':
		bins=[]
		for bin in set(df.zdbin.tolist()):
			bins.append([df[df.zdbin == bin],bin])
		return bins
	if by=='AM/PM':
		AM = df[df.timeobs >= time]
		PM = df[df.timeobs < time]
		return [AM,PM]
