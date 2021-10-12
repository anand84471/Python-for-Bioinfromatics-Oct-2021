#open
# path=r"C:\learning\github\main\Python-for-Bioinfromatics-Oct-2021\day9\result.txt"
list_sequences=["ATAGAA\n","ATAGAT\n"]

file=open("sequences.txt","w")

#write 
file.write("ATGATAGATATGT"+"\n")
file.write("ATGATAGATATGT"+"\n")
file.write("ATGATAGATATGT"+"\n")
file.write("ATGATAGATATGT"+"\n")
file.write("ATGATAGATATGT"+"\n")

for data in list_sequences:
    file.write(data)

#writeline
file.writelines("ATGATAGATATGT"+"\n")
file.writelines(list_sequences)
file.close()