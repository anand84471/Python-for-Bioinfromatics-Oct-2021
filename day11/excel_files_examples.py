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
rows_mortality_gt10=data.loc[data["Mortality Count"]>10]
print(rows_mortality_gt10)




#describe
print(rows_mortality_gt10.describe())


#applying multiple conditions on the coulmns
brain_cancer_data_with_mor_gt_10=data.loc[
    (data["Mortality Count"]>10) & 
    (data["Cancer group/site"]=="Brain Cancer")&
    (data["Year"]>1995)
    ]
print(brain_cancer_data_with_mor_gt_10)


#applying multiple conditions on the coulmns
result=data.loc[
    (data["Mortality Count"]>10) |
    (data["Cancer group/site"]=="Brain Cancer")
    ]
print(result)


#shape ==> getting the shape of excel file(rows and columns)
print(data.shape)
print(data.shape[0]) #no of rows
print(data.shape[1]) #no of coumns



#sorting of the data
result=data.sort_values(['Mortality Count'], ascending = False)
print(result)
result=data.sort_values(['Mortality Count','Year'], ascending = True)
print(result)
# result=data.sort_values(['Mortality Count'],ascending=True).head(10)
# print(result)