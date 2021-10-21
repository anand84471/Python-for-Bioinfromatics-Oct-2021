from Bio import Entrez
from Bio import SeqIO
handle = Entrez.efetch(db="nucleotide", id="AY851612", rettype="gb", retmode="text")
#gb ==> genbank 

print(handle.read())

handle = Entrez.efetch(db="nucleotide", id="AY851612", rettype="fasta", retmode="text")
#print(handle.read())

#saving the sequence information in file
file_to_save=open("result.gb","w")
file_to_save.write(handle.read())
file_to_save.close()




handle = Entrez.efetch(db="nucleotide", id="AY851612", rettype="gb", retmode="text")
record=SeqIO.read(handle,"gb") #seq record


#print(record)
print(record.id) #id
print(record.name) #name
print(record.description) #description
#print(record.seq)



#features
features_seq=record.features
print(features_seq)
print(len(features_seq))

# for feature in features_seq:
#     print(feature.type,"=>",feature.location)

cds_feature=[feature for feature in features_seq if feature.type=="CDS"]
mat_peptides=[feature for feature in features_seq if feature.type=="mat_peptide"]
print(cds_feature)
for feature in cds_feature:
    print(feature.type,"=>",feature.location)

for mat in mat_peptides:
    print(mat.type,"=>",mat.location)



for regions in cds_feature:
    print(regions.location,regions.extract(record.seq).translate())