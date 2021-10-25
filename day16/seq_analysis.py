from Bio import SeqIO
path=r"C:\learning\github\main\Python-for-Bioinfromatics-Oct-2021\day16\result.fasta"
records=SeqIO.parse(path,format="fasta")
#records==> list of SeqRecords
for seq in records:
    print(seq.id)
    print(seq.seq)
    print(seq.description)
    print(len(seq.seq))