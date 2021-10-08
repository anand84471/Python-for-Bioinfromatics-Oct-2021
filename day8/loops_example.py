sequences=["ATAGTA","AATGATATATAGA","ATAGATAG","AATAGAT"]
index=0 #initialization
while index<len(sequences): #condition
    print(sequences[index]) 
    index+=1 #index=index+1 #updation

num=0
while num<10: #0 1 2 3 4
    print(num)
    num=num+1

t_cell_epitopes=["LPVLQV","FGDSVE","VEKGVLPQLEQ","ARTAPH","EIPVA"]

index=0
while index<len(t_cell_epitopes):
    if len(t_cell_epitopes[index])>5:
        print(t_cell_epitopes[index],len(t_cell_epitopes[index]))
    index+=1


