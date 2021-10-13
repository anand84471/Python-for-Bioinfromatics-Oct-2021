#installing pandas
#python -m pip install pandas
#pip install pandas
import pandas as pd

data=pd.read_excel(r"C:\learning\github\main\Python-for-Bioinfromatics-Oct-2021\day10\working_with_excel_files\cancer_data_final.xlsx")

#head #to get the first few rows present in excel file
print(data.head(10))


#tail
print(data.tail(7))


#indexing
print(data[10:20])
