from Bio.Blast import NCBIWWW
#using qblast to work with blastn using GI id.
print("Blast progrma has started....")
result_handle = NCBIWWW.qblast("blastn", "nt", "8332116")
print("Blast progrma has completed....")
print(result_handle.read(),file=open("blast_result.fasta","w")) 