from functions_example import calculate_gc_percentage
list_seq=["AT","ATAGATAGAT","ATAGATAGTAATG"]

handler=open("sequences_details.txt","a")

for seq in list_seq:
    handler.write(seq+"\t"+str(len(seq))+"\t"+str(calculate_gc_percentage(seq))+"\n")

handler.close()