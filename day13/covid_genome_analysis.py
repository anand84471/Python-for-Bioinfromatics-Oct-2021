from Bio import SeqIO
from matplotlib.pyplot import table
path=r"C:\learning\github\main\Python-for-Bioinfromatics-Oct-2021\day12\covid_seq.gb"
covid_seq=SeqIO.read(path,"genbank").seq
print(covid_seq)

aa_chains=set(str(covid_seq.translate(table=2)).split("*"))
lengths=[len(seq) for seq in aa_chains]

# import matplotlib.pyplot as plt
# #plt.hist(lengths)
# plt.plot(lengths)
# plt.show()

#mutation
covid_seq_mut=covid_seq.tomutable()
covid_seq_mut[2:3]="ATGTGT"
print(covid_seq_mut)


covid_seq_mut.transcribe()