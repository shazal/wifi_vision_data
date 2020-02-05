1 - First of all we have got raw wifi data with all the AP distance reading at every location in "wifi.txt". 
Run the "parse_allwifiresults.py" with relevant "wifi.txt" It will output 2 files "wifiaverage.txt" and "wifiminimum.txt". 

2 - Run trilaterate_wholefile.py to get trilatration results. Now if you want trilateration results with minimum wifi
reading use "wifiminimum.txt" or use "wifiaverage.txt" for average readings. If you use minimum name the 
output file to "minimumtrilaterate.txt" or name to "averagetrilaterate.txt" if using average.
You will also need to change the AP positions for relevant location.

For Lab Use:
AP1x = 0
AP1y = 0
AP2x = -6.45
AP2y = 14.8
AP3x = 4.21
AP3y = 14.8

For Class Use:
AP1x = 0
AP1y = 0
AP2x = -2.56
AP2y = 6.24
AP3x = 3.47
AP3y = 6.24

3 - Finally run "process_vision_wifi.py" with the output file you generated in last step and with "vision.txt". 
This file generates plots. Currently only scatter plot generation is uncommented, you can uncomment rest based 
on what you need.

"sanity_trilaterate.py" can be used to make circles and see how off our trilateration results are. Change the distances
according to either "wifiaverage.txt" or "wifiminimum.txt". The AP positions will be same as step 2.

Format of wifi.txt

x y AP_Mac AP_SSID distance_from_AP  (Every AP at every locaiton has around 50 readings)

Format of vision.txt

x y x_measured y_measured z_measured pixel_x pixel_y frame_number object_number


Format of wifiaverage.txt and wifiminimum.txt

x y AP_SSID distance

Format of minimumtrilaterate.txt and averagetrilaterate.txt

x y localized_x localized_y

Format for groundtruth.txt

x y distance_x(inches) distance_z(ft)

Format for Actual_distance_from_APs.txt

x y distance_from1(ft) distance_from2(ft) distance_from3(ft)
