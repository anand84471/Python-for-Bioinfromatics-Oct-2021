#mutation is done by using the slicing
seq="ATGATAGATAATAGAT"
mutated_seq=seq[:2]+"N"+seq[3:]
#              AT   +N + ATAGATAATAGAT
print(seq)
print(mutated_seq)


# from Bio.Seq import MutableSeq
# seq=MutableSeq(seq)
# seq[2]="N"
# seq[4]="U"
# print(seq)