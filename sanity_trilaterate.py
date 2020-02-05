from matplotlib import pyplot as plt
import numpy

distance1 = 2.57348
distance2 = 20.05256
distance3 = 21.091420000000003

AP1x = 0
AP1y = 0
AP2x = -7.18
AP2y = 18.61
AP3x = 3.47
AP3y = 18.61

import localization as lx

P=lx.Project(mode='2D',solver='LSE')


P.add_anchor('anchore_A',(AP1x,AP1y))
P.add_anchor('anchore_B',(AP2x,AP2y))
P.add_anchor('anchore_C',(AP3x,AP3y))

t,label=P.add_target()

t.add_measure('anchore_A',distance1)
t.add_measure('anchore_B',distance2)
t.add_measure('anchore_C',distance3)

P.solve()

# Then the target location is:

print(t.loc)

plt.figure()
ax = plt.gca()
circle = plt.Circle((AP1x, AP1y), radius = distance1, fill=False)
ax.add_artist(circle)
circle1 = plt.Circle((AP2x, AP2y), radius = distance2, fill=False)
ax.add_artist(circle1)
circle2 = plt.Circle((AP3x, AP3y), radius = distance3, fill=False)
ax.add_artist(circle2)
plt.xlim([-20, 20])
plt.ylim([-10, 20])
plt.show()


