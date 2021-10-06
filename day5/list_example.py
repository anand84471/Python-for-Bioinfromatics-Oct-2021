#creating the list

list_example=[]
print(list_example)
names=["Anand","Ajay"]

acc_ids=["AYC101","AYC102","AYC103"]

gc_percentages=[30.4,56.8,98]

print(names,acc_ids,gc_percentages)


#nested lists
records=[1,2,"Anand","TAGAA",35.4,[1,2,3]]
print(records)



#indexing and slicing
#          -3       -2      -1
acc_ids=["AYC101","AYC102","AYC103"]
#          0        1        2
print(acc_ids[0])
print(acc_ids[2])
print(acc_ids[-1])

print(acc_ids[1:3]) #['AYC102', 'AYC103'][0]
print(acc_ids[1:3][0])

