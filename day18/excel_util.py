import pandas as pd
import matplotlib.pyplot as plt
path=r"C:\learning\github\main\Python-for-Bioinfromatics-Oct-2021\day10\working_with_excel_files\cancer_data_final.xlsx"
data=pd.read_excel(path)
all_x=data.loc[data["Cancer group/site"]=="Acute lymphoblastic leukaemia (ALL)"]["Year"]
all_y=data.loc[data["Cancer group/site"]=="Acute lymphoblastic leukaemia (ALL)"]["Mortality Count"]

brain_x=data.loc[data["Cancer group/site"]=="Brain Cancer"]["Year"]
barin_y=data.loc[data["Cancer group/site"]=="Brain Cancer"]["Mortality Count"]