path=r"C:\learning\github\main\Python-for-Bioinfromatics-Oct-2021\day10\blast_result.txt"

file=open(path,"r")

for lines in file.readlines():
    #write code to work with every line
    if  not lines.startswith("#"):
        
        print(lines)


