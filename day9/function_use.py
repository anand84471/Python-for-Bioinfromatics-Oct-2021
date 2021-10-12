seq="ATATAGATAATTAGT"

def calculate_gc_percentage(seq):
    return 100*(seq.count("G")+seq.count("C"))/len(seq)


print(calculate_gc_percentage(seq))