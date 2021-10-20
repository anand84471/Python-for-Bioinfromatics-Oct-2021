from Bio import SeqIO
path=r"C:\learning\github\main\Python-for-Bioinfromatics-Oct-2021\day12\covid_seq.gb"
genbannk_record=SeqIO.read(path,"genbank")

seq=genbannk_record.seq

#print sequence
print(seq)

#gc percentgae
from Bio.SeqUtils import GC
gc_value=GC(seq)
print(gc_value)

#count the motifs
print(seq.count("AGG"))

restriction_enzyme_sites=["ATGT","AAATT","GGG"]

for resitriction_sites in restriction_enzyme_sites:
    print(resitriction_sites,seq.count(resitriction_sites))


#getting the location of motifs
import re
for locations in re.finditer("AAAAATG",str(seq)):
    print(locations.start(),locations.end())

print(type(seq))


#transcribe 
rna=seq.transcribe()
print(rna)

#back trasncibe
dna=rna.back_transcribe()
print(dna)


#complement
complement_dna=seq.complement()
print(complement_dna)


#translation
aa_chains=seq.translate()
print(aa_chains)

ls_aa_chanis=str(aa_chains).split("*")
print(ls_aa_chanis)
print(len(ls_aa_chanis))

unique_aa_chains=set(ls_aa_chanis)
print(len(unique_aa_chains))


