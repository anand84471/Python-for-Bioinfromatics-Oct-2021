#add opertaion
t_cell_epitopes={"LPVLQV","FGDSVE","VEKGVLPQLEQ","ARTAPH","EIPVA"}
t_cell_epitopes.add("FGDSV")
t_cell_epitopes.add("FGDSV") #will not be added
t_cell_epitopes.add("FGDSV") #will not be added
print(t_cell_epitopes)

#discard operation
set_example={1,2,3}
set_example.discard(1)
print(set_example)
t_cell_epitopes.discard("LPVLQV")
print(t_cell_epitopes)