Run the bashscript run.sh like:

bash run.sh [Directory Name] [min/average] [LSE/Linear]

First Argument is the name of the directory in which your files.
Second argument determines whether we are going to take average or min of raw wifi data for pre trilateration purpose.
Third argument decides the trilateration scheme to use.


Format of wifi.txt:

x y AP_Mac AP_SSID distance_from_AP  (Every AP at every locaiton has around 50 readings)

Format of vision.txt:

x y x_measured y_measured z_measured pixel_x pixel_y frame_number object_number

Format of wifiaverage.txt and wifiminimum.txt:

x y AP_SSID distance

Format of minimumtrilaterate.txt and averagetrilaterate.txt:

x y localized_x localized_y

Format for groundtruth.txt:

x y distance_x(m) distance_z(m)

Format for Actual_distance_from_APs.txt:

x y distance_from1(ft) distance_from2(ft) distance_from3(ft)
