seq="ATGCATGCA"

#  A    1    2    3    4    5    6    7    8
#  ×    ↓    ↓    ↓    ↓   ×    ×    ×    ×
# ['A', 'T', 'G', 'C', 'A', 'T', 'G', 'C', 'A']

# ['A', 'T', 'G', 'C', 'A', 'T', 'G', 'C', 'A']
#  ×    ×    ×    ×    ↑    ↑    ↑    ×    ×
# -9   -8   -7   -6   -5   -4   -3   -2   -1


#slicing
#string_name[start:stop]==> returns the part of string from start index to stop-1 index


print(seq[1:5])
print(seq[2:6])
print(seq[4:7])
print(seq[-5:-2])
print(seq[-9:-6])

seq="ATGCATGCA"
# String_name[start:] => will return the value from start index and upto end of string
print(seq[2:])# ⇒  “GCATGCA”
# String_name[:stop] ⇒ will return the value from 0 index and upto stop-1 index 
print(seq[:-2])# ⇒  “ATGCATG”
# String_name[:] ⇒ string_name
print(seq[:])# ⇒ “ATGCATGCA” 



dna_seq="ATGATAGTAGTAGAGATA" 
length=len(dna_seq)
print(dna_seq[:int(length/2)]) #first half part
print(dna_seq[int(length/2):]) #second half part