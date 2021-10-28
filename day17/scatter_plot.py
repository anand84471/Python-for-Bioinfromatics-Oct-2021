import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,10,100)
# plt.scatter(x,np.sin(x))
plt.scatter(x, np.sin(x), c=x, s=100*(np.sin(x)+1), alpha=0.3,
cmap='viridis')
plt.colorbar()

plt.show()
