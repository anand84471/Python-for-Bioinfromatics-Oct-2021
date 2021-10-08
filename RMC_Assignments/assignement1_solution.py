seq=input("Please enter the sequence: ")
# position_of_mutation=int(input("Please enter the position of mutation: "))
# mutated_char=input("Please enter the mutated char: ")
#mutated_seq=seq[:position_of_mutation-1]+mutated_char+seq[position_of_mutation:]
list_converted_seq=list(seq)  #CONVERTING STRIN TO LIST
#print(mutated_seq)
list_converted_seq[2]="NN"
print(list_converted_seq)

muated_seq="".join(list_converted_seq) #CONVERTING LIST TO STRING
print(muated_seq)
