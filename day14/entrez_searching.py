from os import path
from Bio import Entrez
from Bio import SeqIO
Entrez.email="temp@gmail.com"
#Performing search in Entrez
handle = Entrez.esearch(db="nucleotide", retmax=100, term="BRCA", idtype="acc")
record = Entrez.read(handle) #dictionary
handle.close()
print(record) #gives you the list of acessions nos



acc_nos=record["IdList"]
print(acc_nos)

for count,ids in enumerate(acc_nos):
    handle = Entrez.efetch(db="nucleotide", id=ids, rettype="gb", retmode="text")
    record=SeqIO.read(handle,"gb") #seq record
    print(record.description)
    print("Fetching information for id no:-",count)