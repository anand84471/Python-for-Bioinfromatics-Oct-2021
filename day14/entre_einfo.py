from Bio import Entrez
handle = Entrez.einfo() # or esearch, efetch, ...
record = Entrez.read(handle)
print(record) #all the available databases
handle.close()
