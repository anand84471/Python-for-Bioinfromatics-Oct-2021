#creating a function

def function_name(param1,param2,pram3):
    #body of the function
    pass


def calculate_area_of_rectiangle(length,width):
    area=length*width
    return area



#using the function
result=calculate_area_of_rectiangle(4,5)

print(result)


def calculate_gc_percentage(seq):
    return 100*(seq.count("G")+seq.count("C"))/len(seq)


def get_avg_gc_percentage(seq1,seq2):
    gc_per_seq1=calculate_gc_percentage(seq1)
    gc_per_seq2=calculate_gc_percentage(seq2)
    return 0.5*(gc_per_seq1+gc_per_seq2)

result=get_avg_gc_percentage("ATGC","GGG")
print(result)


def calculate_avg_gc_percentage(*sequences):
    count=0
    total_gc_percentage=0
    for seq in sequences:
        total_gc_percentage+=calculate_gc_percentage(seq)
        count+=1
    return total_gc_percentage/count



result=calculate_avg_gc_percentage("ATGATGATA","ATAGTAGATA","ATAGTA")
print(result)