sequences=["ATAGTA","AATGATATATAGA","ATAGATAG","AATAGAT"]

for seq in sequences:
    print(seq)

for seq in sequences:
    print(len(seq))

t_cell_epitopes=["LPVLQV","FGDSVE","VEKGVLPQLEQ","ARTAPH","EIPVA"]

for epitope in t_cell_epitopes:
    if len(epitope)>5:
        print(epitope,len(epitope))