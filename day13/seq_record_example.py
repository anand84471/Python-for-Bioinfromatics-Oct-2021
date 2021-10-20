from Bio import SeqIO
path=r"C:\learning\github\main\Python-for-Bioinfromatics-Oct-2021\day12\covid_seq.gb"
record=SeqIO.read(path,"genbank")  #seqrecord object
#genbank
#fasta
#swiss-prot


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