import matplotlib.pyplot as plt
import numpy as np
from excel_util import brain_x,barin_y,all_y,all_x
fig,axis=plt.subplots(2,2)
x=np.linspace(0,10,100)
axis[0,0].plot(all_x,all_y)
axis[0,1].plot(brain_x,barin_y)
axis[1,0].hist(all_y)
plt.show()


