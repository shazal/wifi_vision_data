import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance
import math
import sys

visionfile = sys.argv[1]
wifitrifile = sys.argv[2]
groundtruthfile = sys.argv[3]

measured = open(visionfile, "r")
wifi = open(wifitrifile, "r")
ground = open(groundtruthfile, "r")

final_arr = []
x_measure_arr = []
z_measure_arr = []
x_ave_arr = []
z_ave_arr = []
x_diff_arr = []
z_diff_arr = []
coordinates = []
x_wifi_arr = []
z_wifi_arr = []
x_wifi_diff = []
z_wifi_diff = []
vision_euclidian = []
wifi_euclidian = []
counter = 0
pixelx = 0
pixely = 0

heuristic_x_arr = []
heuristic_z_arr = []
heuristic_euclidian = []
x_measure_scatter = []
z_measure_scatter = []

for lineinmeasure in measured:
	sep = lineinmeasure.split(" ")
	if sep[0] == "count":
		counter = counter + 1
		line = ground.readline()
		wifiline = wifi.readline()
		words  = line.split(" ")
		x = words[0]
		y = words[1]
		x_measure = float(words[2])
		spl = words[3].split("'");
		z_measure = float (words[3])
		count = int(sep[1])
		total = 0
		x_total = 0.0
		z_total = 0.0
		wifiwords = wifiline.split(" ")
		x_wifi = float(wifiwords[2])
		z_wifi = float(wifiwords[3].split("\n")[0])
	else:
		if total == 0:
			pixelx = float(sep[5])
			pixely = float(sep[6])
		x_cam = float(sep[2])
		z_cam = float(sep[4])
		if x_cam != 0 and z_cam != 0:
			x_total = x_total + x_cam
			z_total = z_total + z_cam

		total = total + 1

		if total == count:
			x_ave = x_total/count
			z_ave = z_total/count

			z_ave = math.sqrt(z_ave * z_ave - x_ave * x_ave)
			
			final_arr.append([x,y,x_measure, z_measure, x_ave, z_ave])
			x_measure_arr.append(abs(x_measure))
			z_measure_arr.append(abs(z_measure))
			x_measure_scatter.append(x_measure)
			z_measure_scatter.append(z_measure)
			x_ave_arr.append(x_ave)
			z_ave_arr.append(z_ave)
			x_diff_arr.append(abs(x_measure-x_ave))
			z_diff_arr.append(abs(z_measure-z_ave))
			coordinates.append(x + y)
			x_wifi_arr.append(x_wifi)
			z_wifi_arr.append(z_wifi)
			x_wifi_diff.append(abs(x_measure-x_wifi))
			z_wifi_diff.append(abs(z_measure-z_wifi))
			p1 = (x_ave, z_ave)
			p2 = (x_wifi, z_wifi)
			p3 = (x_measure, z_measure)
			vision_euclidian.append(distance.euclidean(p1, p3))
			wifi_euclidian.append(distance.euclidean(p2, p3))
			if pixelx < 300 or pixelx > 900 or z_measure > 9:
				heuristic_x_arr.append(x_wifi)
				heuristic_z_arr.append(z_wifi)
				heuristic_euclidian.append(distance.euclidean(p2, p3))
			else:
				heuristic_x_arr.append(x_ave)
				heuristic_z_arr.append(z_ave)
				heuristic_euclidian.append(distance.euclidean(p1, p3))




num_bins = 20
"""
counts, bin_edges = np.histogram (x_diff_arr, bins=num_bins, normed=True)
cdf = np.cumsum (counts)
fig = plt.figure()
fig.suptitle('X displacement Error cdf', fontsize=20)
plt.xlabel('Distance Meters', fontsize=18)
plt.ylabel('CDF', fontsize=16)
plt.plot (bin_edges[1:], cdf/cdf[-1])

plt.show(block=False)
fig.savefig('X_error_cdf.jpg')

counts, bin_edges = np.histogram (z_diff_arr, bins=num_bins, normed=True)
cdf = np.cumsum (counts)
fig = plt.figure()
fig.suptitle('Z displacement Error cdf', fontsize=20)
plt.xlabel('Distance Meters', fontsize=18)
plt.ylabel('CDF', fontsize=16)
plt.plot (bin_edges[1:], cdf/cdf[-1])

plt.show(block=False)
fig.savefig('Z_error_cdf.jpg')

counts, bin_edges = np.histogram (vision_euclidian, bins=num_bins, normed=True)
cdf = np.cumsum (counts)
fig = plt.figure()
fig.suptitle('Euclidian Error cdf', fontsize=20)
plt.xlabel('Distance Meters', fontsize=18)
plt.ylabel('CDF', fontsize=16)
plt.plot (bin_edges[1:], cdf/cdf[-1])

plt.show(block=False)
fig.savefig('Euclidian_error_cdf.jpg')

fig = plt.figure()
plt.scatter(x_measure_arr, x_diff_arr)
fig.suptitle('X Displacement vs Error in X Displacement', fontsize=20)
plt.xlabel('Origional X', fontsize=18)
plt.ylabel('Error in X', fontsize=16)

plt.show(block=False)
fig.savefig('X_vs_error_x.jpg')

fig = plt.figure()
plt.scatter(x_measure_arr, z_diff_arr)
fig.suptitle('X Displacement vs Error in Z', fontsize=20)
plt.xlabel('Origional X', fontsize=18)
plt.ylabel('Error in Z', fontsize=16)

plt.show(block=False)
fig.savefig('X_vs_error_z.jpg')

fig = plt.figure()
plt.scatter(z_measure_arr, x_diff_arr)
fig.suptitle('Z vs Error in X Displacement', fontsize=20)
plt.xlabel('Origional Z', fontsize=18)
plt.ylabel('Error in X', fontsize=16)

plt.show(block=False)
fig.savefig('Z_vsError_in_X.jpg')

fig = plt.figure()
plt.scatter(z_measure_arr, z_diff_arr)
fig.suptitle('Z vs Error in Z', fontsize=20)
plt.xlabel('Origional Z', fontsize=18)
plt.ylabel('Error in Z', fontsize=16)

plt.show(block=False)
fig.savefig('Z_vs_Error_in_Z.jpg')

fig = plt.figure()
plt.scatter(z_measure_arr, vision_euclidian)
fig.suptitle('Z vs Euclidian Error', fontsize=20)
plt.xlabel('Origional Z', fontsize=18)
plt.ylabel('Euclidian Error', fontsize=16)

plt.show(block=False)
fig.savefig('Z_vs_Euclidian.jpg')




num_bins = 20
counts, bin_edges = np.histogram (x_wifi_diff, bins=num_bins, normed=True)
cdf = np.cumsum (counts)
fig = plt.figure()
fig.suptitle('WiFi X displacement Error cdf', fontsize=20)
plt.xlabel('Distance Meters', fontsize=18)
plt.ylabel('CDF', fontsize=16)
plt.plot (bin_edges[1:], cdf/cdf[-1])

plt.show(block=False)
fig.savefig('WiFi_X_error_cdf.jpg')

counts, bin_edges = np.histogram (z_wifi_diff, bins=num_bins, normed=True)
cdf = np.cumsum (counts)
fig = plt.figure()
fig.suptitle('WiFi Z displacement Error cdf', fontsize=20)
plt.xlabel('Distance Meters', fontsize=18)
plt.ylabel('CDF', fontsize=16)
plt.plot (bin_edges[1:], cdf/cdf[-1])

plt.show(block=False)
fig.savefig('Wifi_Z_error_cdf.jpg')

counts, bin_edges = np.histogram (wifi_euclidian, bins=num_bins, normed=True)
cdf = np.cumsum (counts)
fig = plt.figure()
fig.suptitle('WiFi Euclidian Error cdf', fontsize=20)
plt.xlabel('Distance Meters', fontsize=18)
plt.ylabel('CDF', fontsize=16)
plt.plot (bin_edges[1:], cdf/cdf[-1])

plt.show(block=False)
fig.savefig('WiFi_Euclidian_error_cdf.jpg')


fig = plt.figure()
plt.scatter(x_measure_arr, x_wifi_diff)
fig.suptitle('WiFi X Displacement vs Error in X Displacement', fontsize=20)
plt.xlabel('Origional X', fontsize=18)
plt.ylabel('Error in X', fontsize=16)

plt.show(block=False)
fig.savefig('WiFi_X_vs_error_x.jpg')

fig = plt.figure()
plt.scatter(x_measure_arr, z_wifi_diff)
fig.suptitle('WiFi X Displacement vs Error in Z', fontsize=20)
plt.xlabel('Origional X', fontsize=18)
plt.ylabel('Error in Z', fontsize=16)

plt.show(block=False)
fig.savefig('WiFi_X_vs_error_z.jpg')

fig = plt.figure()
plt.scatter(z_measure_arr, x_wifi_diff)
fig.suptitle('WiFi Z vs Error in X Displacement', fontsize=20)
plt.xlabel('Origional Z', fontsize=18)
plt.ylabel('Error in X', fontsize=16)

plt.show(block=False)
fig.savefig('WiFi_Z_vs_Error_in_X.jpg')

fig = plt.figure()
plt.scatter(z_measure_arr, z_wifi_diff)
fig.suptitle('WiFi Z vs Error in Z', fontsize=20)
plt.xlabel('Origional Z', fontsize=18)
plt.ylabel('Error in Z', fontsize=16)

plt.show(block=False)
fig.savefig('WiFi_Z_vs_Error_in_Z.jpg')

fig = plt.figure()
plt.scatter(z_measure_arr, wifi_euclidian)
fig.suptitle('WiFi Z vs Euclidian Error', fontsize=20)
plt.xlabel('Origional Z', fontsize=18)
plt.ylabel('Euclidian Error', fontsize=16)

plt.show(block=False)
fig.savefig('WiFi_Z_vs_Euclidian.jpg')
"""


for i in range(len(wifi_euclidian)):
	print(wifi_euclidian[i])

for i in range(len(x_ave_arr)):
	print(str(x_ave_arr[i]) + " " + str(z_ave_arr[i]))

for i in range(len(wifi_euclidian)):
	print(vision_euclidian[i])


fig = plt.figure()
wifi = plt.scatter(x_wifi_arr, z_wifi_arr,  marker = "+", s = 125)
vision = plt.scatter(x_ave_arr, z_ave_arr,  marker = "8", s = 125)
Origional = plt.scatter(x_measure_scatter, z_measure_scatter,  marker = "v", s = 125)
fig.suptitle('All Data Mapped', fontsize=20)
plt.xlabel('X Axis', fontsize=18)
plt.ylabel('Z Axis', fontsize=16)
plt.legend((wifi, vision, Origional),
           ('WiFi', 'Vision', 'Actual'),
           scatterpoints=1,
           loc='upper left',
           ncol=3,
           fontsize=10)

for i in range(len(x_wifi_arr)):
	print(i)
	plt.annotate(i, (x_wifi_arr[i], z_wifi_arr[i]), size=18)
	plt.annotate(i, (x_ave_arr[i], z_ave_arr[i]), size=18)
	plt.annotate(i, (x_measure_scatter[i], z_measure_scatter[i]), size=18)

plt.show()
fig.savefig('All_Data_Mapped.jpg')

