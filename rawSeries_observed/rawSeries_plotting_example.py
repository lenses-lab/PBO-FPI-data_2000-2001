import os, sys
import numpy as np
import matplotlib.pyplot as plt
from rawSeriesParser import *

## Various constants ##
#----------------------
# Grabs path to this script
datapath = os.path.abspath(os.path.dirname(sys.argv[0]))+"/" 
# Defines the grey color of the PM plot
grey = '#777777' 
# Defines the subplot grid
gridsz = [2,2]

## Set up plots ##
#-----------------
fig = plt.figure()
grid = plt.GridSpec(gridsz[0],gridsz[1])
axes=[]
for x in range(0,gridsz[0]):
	for y in range(0,gridsz[1]):
		axes.append(fig.add_subplot(grid[x,y]))
for ax in axes:
	ax.set_xscale('linear')
	ax.set_xlim(1,2500)
	ax.set_ylim(0,22)
	ax.set_xlabel("Shadow Altitude (km)")
	ax.set_ylabel(r"H-$\alpha$ Intensity (R)")
	
## Retrieve and Plot Data ##
#---------------------------
for i,ser_no in enumerate(['11','5','6','7']):
	datafile = "rawSeries_observed/s"+ser_no+"/s"+ser_no+"_observation.dat"
	
	# use the rawseries class defined in rawSeriesParser to parse datafile into a Pandas dataframe
	s_df = rawseries(datapath+datafile).df
	
	# Make zdbin and galactic longitude cuts as in Mierkiewicz et al. 2006
	# Look at Pandas documentation for more on manipulating Pandas dataframes
	s_cut = s_df[(s_df.zdbin<4)&((s_df.gallon>10)|(s_df.gallon<-10))]
	
	# Sort data by time of observation and then split into AM/PM bins at 6:00 UTC
	# These functions are included in rawSeriesParser
	s_sorted = sortby(s_cut,'timeobs')
	AMbin,PMbin = splitby(s_sorted,'AM/PM',time=6)

	# Plot x=shadow altitude, y=intensity
	axes[i].plot(AMbin.shdalt,AMbin.igeo,'kx',markersize='5',markerfacecolor='None',label="AM, PBO")
	axes[i].plot(PMbin.shdalt,PMbin.igeo,'ko',markersize='5',markerfacecolor='None',label="PM, PBO",markeredgecolor=grey)

# Add a legend
hs,lgds = axes[gridsz[1]-1].get_legend_handles_labels()
lgd = axes[gridsz[1]-1].legend(hs,lgds,fontsize=10,numpoints=1)

# Show plot
fig.tight_layout()
plt.show()
