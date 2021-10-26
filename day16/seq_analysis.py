from Bio import SeqIO
path=r"C:\learning\github\main\Python-for-Bioinfromatics-Oct-2021\day16\result.fasta"
records=SeqIO.parse(path,format="fasta")
#records==> list of SeqRecords
for seq_record in records:
    print(seq_record.id) #accession id
    print(seq_record.seq) #getting the complete sequence
    print(seq_record.description) #desciption
    print(len(seq_record.seq)) #working with the sequence
    print(seq_record.seq.transcribe())

