#donwload muscle
#https://www.drive5.com/muscle/downloads.htm
import os
os.chdir("C:\learning\github\main\Python-for-Bioinfromatics-Oct-2021\day16")
from Bio.Align.Applications import MuscleCommandline
path=r"C:\learning\github\main\Python-for-Bioinfromatics-Oct-2021\day16\result.fasta"
muscle_cline = MuscleCommandline(input=path, out="muscle_python_result.txt")
#muscle -in opuntia.fasta -out opuntia.txt
stdout, stderr = muscle_cline()
