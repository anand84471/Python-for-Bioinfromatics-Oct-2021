path=r"C:\learning\github\main\Python-for-Bioinfromatics-Oct-2021\day10\blast_result.txt"
file=open(path,"r")

#read
#print(file.read())

#readline
# print(file.readline())
# print(file.readline())

#readlines
for lines in file.readlines():
    print(lines)
