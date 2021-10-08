seq_records={
    "YC1":"ATAGATGATAAGA",
    "YC2":"ATGTTATATATAT"
}
print(seq_records)

#adding new value to dict
seq_records["YC3"]="ATGATAGATAATA"
print(seq_records)


#getting all the keys

print(seq_records.keys())


#getting all the values
print(seq_records.values())


#getting length of dict
print(len(seq_records))



dict_example={
    "name":"Anand",
    "email":"temp@gmail.com"
}
dict_example["phone"]="123"
dict_example["address"]="Noida"
print(len(dict_example))


# clear() :Removes all the elements from the dictionary
# copy(): Returns a copy of the dictionary
