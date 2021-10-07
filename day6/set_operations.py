t_cell_epitopes={"LPVLQV","FGDSVE","VEKGVLPQLEQ","ARTAPH","EIPVA"}
b_cell_epitopes={"ARTAPH","IQYG","EIPVA"}


#all the available epitopes

all_epitopes=t_cell_epitopes|b_cell_epitopes
print(len(all_epitopes))

#common eitopes

common_epitopes=t_cell_epitopes&b_cell_epitopes
print(common_epitopes) #all the epitopes that are present in bcell but in tcell

#all the epitopes that are present in tcell but in bcell
print(t_cell_epitopes-b_cell_epitopes)

#all the epitopes that are present in bcell but in tcell
print(b_cell_epitopes-t_cell_epitopes)


