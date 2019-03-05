## selectSeries_observed
This is the set  of 8 PBO series datasets that passed the cuts applied in diurnal asymmetry analysis (outlined in Gallant et al. 2018).  The format includes pointing information, but the intensity measurements may be untrustworthy. Use 'rawSeries_observed' if interested in intensity measurements. Use 'selectSeries_observed' if interested in pointing information. 

Each series includes a 's#_start_compilation.dat' file that is a compilation of all '*_start.dat' files for each series. These pointings correspond to the beginning of the observation, not the midpoint. The dates included in each compilation file follow the JGR paper by Mierkiewicz et al. 2012. 

The values are tab-separated and each three rows makes up one datapoint.
* The first row includes (in order) a sequential index, exposure time [sec], observation time [hrs since midnight], target azimuth, target zenith distance, and solar azimuth.
* The second row includes (in order) solar zenith distance, the sun-target azimuthal difference, shadow altitude [km], zenith distance bin, galactic latitude, and galactic longitude.
* The third row includes (in order) VLSR, observed intensity [Rayleighs], observed doppler width, intensity error, and doppler width error.

Zenith Distance Bin ("zdbin") and Galactic Longitude ("gallon") cuts have not been applied.

The SeriesParser.py python script will be helpful in parsing the selectSeries_observed files.
