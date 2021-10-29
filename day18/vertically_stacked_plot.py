import matplotlib.pyplot as plt
import numpy as np
from excel_util import brain_x,barin_y,all_y,all_x
x=np.linspace(1,10,100)
# fig, axs = plt.subplots(2)
fig, axs = plt.subplots(1,3)
fig.suptitle("Plot examples")
axs[0].plot(brain_x, barin_y)
axs[1].plot(all_x,all_y)
plt.show()
