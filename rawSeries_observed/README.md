## rawSeries_observed
This is the set of all 20 PBO series datasets in a format that includes limited header information (specifically, no pointing information) and sorted into directories based on the series dates in the JGR paper by Mierkiewz et al. 2012. Pointing information was provided for select series, located in the selectSeries_observed directory in this repository.

The values are tab separated and include two rows of values per data point.
* First row includes (in order) __exposure time__ [sec], __shadow altitude__ [km], __intensity__ [Rayleighs], __observation time__ [hours from midnight], __zenith distance bin__, and __observed line center__ [bins].
* Second row includes (in order) __observed doppler width__ [bins], __percentage of cascade__ [%], __galactic longitude__, __VLSR__, and __slope__.

Each series includes a 's#_observation.dat' file that is a compilation of all of the '*_d.out' files for each series. The 'd' in the filename refers to the final stage of data processing done by Dr. Ed Mierkiewicz. 

Zenith Distance Bin ("zdbin") and Galactic Longitude ("gallon") cuts have not been applied.

See the RawSeriesParser.py python class for help with parsing these files.
* The following python dependencies are required to use RawSeriesParser.py: os, sys, numpy, pandas
* To use the functions defined in rawSeriesParser in a script, include this statement with your imports: "from rawSeriesParser import *"
* See rawSeries_plotting_example.py for an example script using the rawSeriesParser
