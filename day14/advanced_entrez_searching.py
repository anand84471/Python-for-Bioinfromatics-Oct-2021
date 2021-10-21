from Bio import Entrez
Entrez.email="akr.cpibtc@gmail.com"
handle = Entrez.esearch(db="protein", term="((108[BioProject] OR 10800[BioProject]))" ,  retmax="40" )
record = Entrez.read(handle)
print(record)