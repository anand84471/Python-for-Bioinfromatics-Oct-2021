import pandas as pd
import matplotlib.pyplot as plt
path=r"C:\learning\github\main\Python-for-Bioinfromatics-Oct-2021\day10\working_with_excel_files\cancer_data_final.xlsx"
data=pd.read_excel(path)
x=data.loc[data["Cancer group/site"]=="Brain Cancer"]["Year"]
y=data.loc[data["Cancer group/site"]=="Brain Cancer"]["Mortality Count"]
# plt.scatter(x, y, c=x, s=100*(y), alpha=0.1)
#plt.errorbar(x,y,10)
plt.errorbar(x,y,0.1*y)
#alph is for transparency
#plt.colorbar()
plt.show()

