# Further investigation into HadISD data auto-correlations 

Figures showing the ACF-1 indicator for the HadISD time-series data. An
interpolated version of the hourly data is used to fit the missing
points. Figures [1](#F-pca-ten)
 and [2](#F-pca-twenty)
 show the first EOF score of the data, along
with ACF-1 indicators calculated using sliding windows of lengths
10-days and 20-days resp. Figures [3](#F-all-five)
 to [5](#F-all-twenty)
 show all six time series (from six stations
located around south Florida) along with the ACF-1 indicators (which use
windows of length 5-days, 10-days and 20-days resp.).

# Looking at the Durbin-Watson statistic.

Figure [6](#DurbinWatson)
shows the Durbin-Watson statistic and the ACF-1 indicator both
calculated in a five-day sliding window. It appears that the two are
scaled mirror-images of each other. This may or may not be interesting,
but it is *intriguing*.

![First EOF score of the six time series shown with the ACF-1 indicator
with a ten day (240-point) sliding
window.](../images/florida_pca_tenday.png){#F-pca-ten


![Same as figure [1](#F-pca-ten)
 but with a twenty day (480 point)
window.](../images/florida_pca_twentyday.png){#F-pca-twenty


![All six time series plotted together (top) along with the six
corresponding ACF-1 indicators (bottom) using a five-day (120 point)
sliding window.](../images/florida_all_fiveday.png){#F-all-five


![All six time series plotted together (top) along with the six
corresponding ACF-1 indicators (bottom) using a ten-day (240 point)
sliding window.](../images/florida_all_tenday.png){#F-all-ten


![All six time series plotted together (top) along with the six
corresponding ACF-1 indicators (bottom) using a twenty-day (480 point)
sliding window.](../images/florida_all_twentyday.png){#F-all-twenty


![The ACF-1 indicator and the Durbin-Watson statistic shown together for
the first EOF score data. Both are calculated in a backward-looking
sliding window of length 120 points (five days).
](../images/DurbinWatson.png)
