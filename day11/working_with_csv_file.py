import pandas as pd
path=r"C:\learning\github\main\Python-for-Bioinfromatics-Oct-2021\day10\working_with_excel_files\gene_expression_data.csv"

data=pd.read_csv(path)

print(data)

print(data.describe())