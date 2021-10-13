import pandas as pd
#set up of pandas
excel_file_path="cancer_data_final.xlsx"
excel_data=pd.read_excel(excel_file_path,engine="openpyxl")
# print(excel_data)


#head => to get the first few rows
print(excel_data.head(10))

#tail => to get the last few rows
print(excel_data.tail())
print(excel_data.tail(10))

#describe



#shape ==> getting the shape of excel file(rows and columns)
print(excel_data.shape)
print(excel_data.shape[0]) #no of rows
print(excel_data.shape[1]) #no of coumns


#describe
print(excel_data.describe())


#reading a particualr coumn #excel_data[["column name"]]
year_data=excel_data[["Year"]]
print(year_data)

#reading multiple columns
year_vs_mortality_count=excel_data[["Year","Mortality Count"]]
print(year_vs_mortality_count)

#creating excel file from pandas

# year_vs_mortality_count.to_excel("year vs mortality count.xlsx",engine="openpyxl")

#creating csv file 
# year_vs_mortality_count.to_csv("year vs mortality count.csv")


#getting unique data of any column
years=excel_data["Year"]
unique_years=set(years)
print(len(unique_years))


#slicing
data_from_10_to_20=excel_data[10:20]
# data_from_10_to_20=excel_data[10:] #stop value==> go upto end
print(data_from_10_to_20)

#filering the data
# data=excel_data.loc [ excel_data['Mortality Count']>10]
data=excel_data.loc[excel_data["Cancer group/site"]=="Brain Cancer"]
print(data)


#sorting of the data
result=excel_data.sort_values(['Mortality Count'], ascending = False)
result=excel_data.sort_values(['Mortality Count','Year'], ascending = True)

result=excel_data.sort_values(['Mortality Count'],ascending=True).head(10)
print(result)



#applying multiple filter 
# data=excel_data.loc [ excel_data['Mortality Count']>10]
data=excel_data.loc[(excel_data["Cancer group/site"]=="Brain Cancer") &
                    (excel_data['Mortality Count']>10)]
print(data)
data.to_excel("filtered data.xlsx",engine="openpyxl")
