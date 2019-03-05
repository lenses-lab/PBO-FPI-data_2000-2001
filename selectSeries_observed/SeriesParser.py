import os, sys
import numpy as np
import pandas as pd

class series:
	def __init__(self, datapath):
		## Open .dat file
		id = open(datapath)
		lines = id.readlines()[1:]
		keys = ['seq','exptime', 'timeobs', 'targaz', 'targzd', 'sunaz', 
				'sunzd', 'diffaz', 'shdalt', 'zdbin', 'glat', 'glon', 
				'vlsr', 'igeo', 'dopw', 'err_igeo', 'err_dopw']
		d = []
		i = 0
		for line in lines:
			i = i + 1
			if i==1:
				first = line.split()
			if i==2:
				second = line.split()
			if i==3:
				third = line.split()
				dpt = [float(x) for x in first+second+third]
				d.append(dpt)
				i=0
		data = np.array(d)
		self.df = pd.DataFrame(data,columns=keys)

def sortby(df, by):
	keys = ['seq','exptime', 'timeobs', 'targaz', 'targzd', 'sunaz', 
			'sunzd', 'diffaz', 'shdalt', 'zdbin', 'glat', 'glon', 
			'vlsr', 'igeo', 'dopw', 'err_igeo', 'err_dopw']

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
			bins.append(df[df.zdbin == bin])
		return bins
	if by=='AM/PM':
		AM = df[df.timeobs >= 6]
		PM = df[df.timeobs < 6]
		return [AM,PM]

def series2los(seriesdf,fout):
	# Susan's WHAM driver (driver_WHAMSUSANZEN.dat) looks for four input columns:
	# SZA, ZNTH, AZI, HSHAD
	sza = seriesdf.sunzd.tolist()
	znth = seriesdf.targzd.tolist()
	azi = seriesdf.diffaz.tolist()
	hshad = seriesdf.shdalt.tolist()
	rows = zip(sza,znth,azi,hshad)
	
	# The driver also looks for a header with five values:
	# (# of rows), (line label), (resonance wavelength), (branching ratio), (solar line center flux)
	n_rows = seriesdf.shape[0]
	llbl = 2
	waveln = 1025.72
	fluorb = 0.882
	fluxc = 1e9
	
	# Write LOS file
	id = open(fout,'w')
	id.write('%i\t%i\t%.3e\t%.3e\t%.4e\n'%(n_rows,llbl,waveln,fluorb,fluxc))
	for row in rows:
		id.write('%.1f    %.1f    %.1f    %.3f\n'%row)
	id.close()
	return None
