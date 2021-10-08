dict_example={}
person_details={
    "name":"Anand",
    "email":"anand.kumar@readmycourse.com",
    "phone":"12345",
    "address":"Noida"
 }

 #getting the value
#syntax: dict_name[key_name]
print(person_details["email"])
print(person_details["phone"])


details={
    "phone_no":person_details["phone"],
    "email_id":person_details["email"]
}

print(details)




sequences={
    "2765658":"CGTAACAAGGTTTCCGTAGGTGAACCTGCGGAAGGATCATTGATGAGACCGTGGAATAAACGATCGAGTG",
    "2765657":"CGTAACAAGGTTTCCGTAGGTGAACCTGCGGAAGGATCATTGTTGAGACAACAGAATATATGATCGAGTG"
}

print(sequences["2765657"].count("A"))
print(sequences["2765658"].count("T"))


#EDITING
person_details={
    "name":"Anand",
    "email":"anand.kumar@readmycourse.com",
    "phone":"12345",
    "address":"Noida"
 }
#syntax
#dict_name[key_name]=new_value
person_details["name"]="Ajay"
print(person_details)