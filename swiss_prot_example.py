from Bio import ExPASy
from Bio import SeqIO
handler = ExPASy.get_sprot_raw('O23729')
# seq_record=SeqIO.read(handler,"swiss")
# print(seq_record)
print(handler.read())