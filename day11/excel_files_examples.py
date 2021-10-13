import pandas as pd

path=r"C:\learning\github\main\Python-for-Bioinfromatics-Oct-2021\day10\working_with_excel_files\cancer_data_final.xlsx"
data=pd.read_excel(path)

#filtering the columns
list_of_required_columns=["Year","Mortality Count"]
year_vs_motality_count=data[list_of_required_columns]
print(year_vs_motality_count)

#saving the file
year_vs_motality_count.to_excel("Year vs mortailty count.xlsx")
year_vs_motality_count.to_csv("Year vs mortailty count.csv")


#applying conditions on the coulmns

