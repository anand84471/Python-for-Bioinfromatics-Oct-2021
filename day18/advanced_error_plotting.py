import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(1,10,100)
plt.errorbar(x,np.sin(x),np.sin(x)-np.sin(x-1),color='black',
               elinewidth=3,capsize=10,ecolor='red')
plt.show()
