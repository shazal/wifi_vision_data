import sys

wififile = sys.argv[1]
wifiaveragefile = sys.argv[2]
wifiminimumfile = sys.argv[3]

labresults = open(wififile, "r")
averagefile = open(wifiaveragefile, "w")
minimumfile = open(wifiminimumfile, "w")

lastAP = ""
lastx = ""
lasty = ""
maincount = 0
minimum = 0.0
average = 0.0
count = 0
for line in labresults:
	
	words = line.split(" ")
	currentx = words[0]
	currenty = words[1]
	currentAP = words[3]
	distance = float(words[4])
	
	if maincount == 0:
		lastx = currentx
		lasty = currenty
		lastAP = currentAP
		maincount = maincount + 1
		minimum = distance
	print (lastx)
	print(currentx)
	print (lasty)
	print(currenty)
	print (lastAP)
	print(currentAP)

	if lasty == currenty and lastAP == currentAP:
		count = count + 1
		if distance <= minimum:
			minimum = distance
		average = average + distance
		lastx = currentx
		lasty = currenty
		lastAP = currentAP
	else:
		finaldistance = average/count
		averagefile.write(lastx + " " + lasty + " " + lastAP + " " + str(finaldistance) + "\n")
		minimumfile.write(lastx + " " + lasty + " " + lastAP + " " + str(minimum) + "\n")

		average = distance
		minimum = distance
		count = 1
		lastx = currentx
		lasty = currenty
		lastAP = currentAP


finaldistance = average/count
averagefile.write(lastx + " " + lasty + " " + lastAP + " " + str(finaldistance) + "\n")
minimumfile.write(lastx + " " + lasty + " " + lastAP + " " + str(minimum) + "\n")
