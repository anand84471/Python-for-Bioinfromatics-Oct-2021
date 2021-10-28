import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,10,100)
# plt.plot(x, np.sin(x - 0), color='blue') # specify color by name
# plt.plot(x, np.sin(x - 2), color='0.75') # Grayscale between 0 and 1 {0 is darker, 1 is brighter}
# plt.plot(x, np.sin(x - 3), color='#FFDD44') # Hex code (RRGGBB from 00 to FF)
# plt.plot(x, np.sin(x - 4), color=(1.0,0.2,0.3)) # RGB tuple, values 0 and 1

# plt.plot(x,np.sin(x),linestyle="solid")
# plt.plot(x,np.sin(x-1),linestyle="dotted")
# plt.plot(x,np.sin(x-2),linestyle="dashdot")
# plt.plot(x,np.sin(x-4),linestyle="dashed")

plt.plot(x,np.sin(x),"v",label="SIN(X)",markersize=10) #solid
plt.plot(x,np.sin(x-1),"p",label="SIN(X-1)",markersize=20) #dashed
plt.plot(x,np.sin(x-2),linestyle="-.",label="SIN(X-2)") #dashdot
plt.plot(x,np.sin(x-4),linestyle=":",label="SIN(X-3)") #dotted

#line markers
# character	description
# '-'	solid line style
# '--'	dashed line style
# '-.'	dash-dot line style
# ':'	dotted line style
# '.'	point marker
# ','	pixel marker
# 'o'	circle marker
# 'v'	triangle_down marker
# '^'	triangle_up marker
# '<'	triangle_left marker
# '>'	triangle_right marker
# '1'	tri_down marker
# '2'	tri_up marker
# '3'	tri_left marker
# '4'	tri_right marker
# 's'	square marker
# 'p'	pentagon marker
# '*'	star marker
# 'h'	hexagon1 marker
# 'H'	hexagon2 marker
# '+'	plus marker
# 'x'	x marker
# 'D'	diamond marker
# 'd'	thin_diamond marker
# '|'	vline marker
# '_'	hline marker

plt.legend()
plt.show()

