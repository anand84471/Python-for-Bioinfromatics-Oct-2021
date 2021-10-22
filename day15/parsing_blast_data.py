from Bio.Blast import NCBIWWW,NCBIXML
from Bio import SeqIO
from Bio import Entrez
from Bio import SeqIO
Entrez.email="akr.cpibtc@gmail.com"
path=r"C:\learning\github\main\Python-for-Bioinfromatics-Oct-2021\day15\blast_result.fasta"
E_VALUE_THRESH=0.001
handle=open(path)
data=NCBIXML.parse(handle)
blast_data=next(data)
id=[]
for alignment in blast_data.alignments:
    print(dir(alignment))
    for hsp in alignment.hsps:
        print(dir(hsp))
        if hsp.expect < E_VALUE_THRESH:
            id.append(alignment.accession)
            print("****Alignment****")
            print("sequence:", alignment.title)
            path("id",alignment.id)
            print("length:", alignment.length)
            print("e value:", hsp.expect)
            print(hsp.query[0:75] + "...")
            print(hsp.match[0:75] + "...")
            print(hsp.sbjct[0:75] + "...")


ids=[id.accession for id in blast_data.alignments]

# ids=[]
# for id in blast_data.alignments:
#     ids.append(id.accession)
print(ids)

file=open("blast_hit_sequences.fasta","w")
for id in ids:
    print("Downloading sequence for ",id)
    handle = Entrez.efetch(db="nucleotide", id=id, rettype="gb", retmode="text")
    file.write(handle.read())
file.close()
