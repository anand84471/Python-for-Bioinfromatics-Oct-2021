from Bio import Entrez 
handler=Entrez.egquery(term="biopython")
record=Entrez.read(handler)
for row in record["eGQueryResult"]:
    print(row)