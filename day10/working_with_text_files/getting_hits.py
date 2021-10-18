path=r"C:\learning\github\main\Python-for-Bioinfromatics-Oct-2021\day10\blast_result.txt"

file=open(path,"r")
EVALUE_C=1.77e-62
IDENTITY_C=75

#initializing an empty to save the result
hits=[]

# for lines in file.readlines():
#     #write code to work with every line
#     if  not lines.startswith("#"): 
#         hits.append(lines.split()[1])


for lines in file.readlines():
    #write code to work with every line
    if  not lines.startswith("#") and float(lines.split()[2])>IDENTITY_C and float(lines.split()[-2])<EVALUE_C: 
        hits.append(lines.split()[1])


print(hits)
print(len(hits))


print("---".join(hits))

line="BE037100.1	XM_016034586.2	76.399	572	111	19	57	619	164	720	1.75e-72	287"

print(line.split())

#['BE037100.1', 'XM_016034586.2', '76.399', '572', '111', '19', '57', '619', '164', '720', '1.75e-72', '287']
#   0               1                2                                                        -2