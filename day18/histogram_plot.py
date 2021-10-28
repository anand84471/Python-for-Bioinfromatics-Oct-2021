import matplotlib.pyplot as plt
from excel_util import barin_y,all_y,all_x
plt.hist(all_y,alpha=0.3)
plt.hist(barin_y,alpha=0.3)
plt.show()