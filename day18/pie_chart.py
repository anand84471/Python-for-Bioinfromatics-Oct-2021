import matplotlib.pyplot as plt
from numpy.lib.function_base import angle
from excel_util import barin_y,all_y,all_x,brain_x
plt.pie(barin_y,labels=brain_x,radius=1.4)
plt.show()