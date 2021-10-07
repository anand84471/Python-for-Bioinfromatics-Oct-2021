# clear()   Removes all the elements from the list
list_example1=["ATGATA","ATGATA"]
list_example1.clear()
print(list_example1)
# copy()    Returns a copy of the list
orginal_list=["ATGC","ATT"]
#list_copy=orginal_list
list_copy=orginal_list.copy()
list_copy.clear()
print(orginal_list)
print(list_copy)
# count()   Returns the number of elements with the specified value
lis_example=[1,1,2,3,4]
print(lis_example.count(1))

sequneces=["ATGC","ATCGTAA","ATGC"]

print(sequneces.count("ATCGTAA"))
# index()   Returns the index of the first element with the specified value
sequneces=["ATGC","ATCGTAA","ATGC"]
#print(sequneces.index("ATGCS")) #It is not safe to use
print("ATGC" in sequneces)


#append() inserts the pecified data at the end
list_example=[1,2]
list_example.append(3)
list_example.append(4)
list_example.append(5)
print(list_example)

# insert()  Adds an element at the specified position
sequneces=["ATGC","ATCGTAA","ATGC"]
sequneces.insert(1,"AAA")
print(sequneces)
# pop() Removes the last element
sequneces=["ATGC","ATCGTAA","ATGC"]
deleted_data=sequneces.pop()
print(deleted_data,sequneces)
deleted_data=sequneces.pop()
print(deleted_data,sequneces)
# reverse() Reverses the order of the list
data=[1,2,3]
data.reverse()
print(data)
# sort()    Sorts the list in the ascending order
data=[30.4,67.8,90.8,10,89]
data.sort()
print(data)

data.reverse()
print(data)