wifimin = open("wifiminimum.txt", "r")
wifitri = open("minimumtrilateration.txt", "a")


count = 0
distance1 = 0.0
distance2 = 0.0
distance3 = 0.0
"""
AP positions LAB
AP1x = 0
AP1y = 0
AP2x = -7.18
AP2y = 18.61
AP3x = 3.47
AP3y = 18.61
"""

# AP positions Class
AP1x = 0
AP1y = 0
AP2x = -6.45
AP2y = 14.8
AP3x = 4.21
AP3y = 14.8
import localization as lx

for line in wifimin:
	words = line.split(" ")
	print(words)
	x = words[0]
	y = words[1]
	AP = words[2]
	print(AP)
	if AP == "wifi1fortest":
		distance1 = float(words[3])
	elif AP == "wifi2fortest":
		distance2 = float(words[3])
	elif AP == "wifi3fortest":
		distance3 = float(words[3])
	count = count + 1

	if count == 3:
		"""
		va = ((distance2*distance2-distance3*distance3) - (AP2x*AP2x-AP3x*AP3x) - (AP2y*AP2y-AP3y*AP3y)) / 2
		vb = ((distance2*distance2-distance1*distance1) - (AP2x*AP2x-AP1x*AP1x) - (AP2y*AP2y-AP1y*AP1y)) / 2
		temp1 = vb*(AP3x-AP2x) - va*(AP1x-AP2x)
		temp2 = (AP1y-AP2y)*(AP3x-AP2x) - (AP3y-AP2y)*(AP1x-AP2x)
		resulty = temp1 / temp2;
		resultx = (va - resulty*(AP3y-AP2y)) / (AP3x-AP2x);
		"""
		
		P=lx.Project(mode='2D',solver='LSE')
		P.add_anchor('anchore_A',(AP1x,AP1y))
		P.add_anchor('anchore_B',(AP2x,AP2y))
		P.add_anchor('anchore_C',(AP3x,AP3y))

		t,label=P.add_target()

		t.add_measure('anchore_A',distance1)
		t.add_measure('anchore_B',distance2)
		t.add_measure('anchore_C',distance3)

		P.solve()

		resultx = t.loc.x
		resulty = t.loc.y

		wifitri.write(x + " " + y + " " + str(resultx) + " " + str(resulty) + "\n")
		count = 0

    
