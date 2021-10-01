seq="AATGATGATaatTAG"
# upper()==>convert sequences to upper case
print(seq.upper())
# lower()==>convert sequences to lower case
print(seq.lower())
# count() ==>gives you the count of chars
seq="ATGCCACC"
print(seq.count("A"))
print(seq.count("C"))
print(seq.count("CC"))
seq="ATGC"
gc_percent=100*(seq.count("G")+seq.count("C"))/len(seq)
print(gc_percent)
# find()==>to find first occurrence of character

seq="ATGTATAGTAGATAATTGT"
print(seq.find("A"))
print(seq.find("T"))
print(seq.find("ATAATTGT"))


dna_Seq="attgatattatgtaa"
res_enz_site="atgt"
print(dna_Seq.find(res_enz_site))

# replace()==> to replace a character with any specific character
seq="ATGC"
print(seq.replace("A","N"))

seq="ATTT"
print(seq.replace("T","A"))

# [::-1]==>to reverse the sequence

dna_seq="atgc"
print(dna_seq[::-1])
