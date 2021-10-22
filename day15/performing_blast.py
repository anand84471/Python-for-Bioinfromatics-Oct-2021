from Bio.Blast import NCBIWWW,NCBIXML
from Bio import SeqIO
fasta_file=open(r"C:\learning\github\main\Python-for-Bioinfromatics-Oct-2021\covid_seq.fasta","r").read()
#SeqIO.convert(r"C:\learning\github\main\Python-for-Bioinfromatics-Oct-2021\day12\covid_seq.gb","genbank","covid_seq.fasta","fasta")
#qblast using fasta file
handler=NCBIWWW.qblast("blastn","nt",fasta_file)
print(handler.read())