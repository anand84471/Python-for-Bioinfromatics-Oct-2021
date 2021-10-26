# from Bio import AlignIO
# alignment = AlignIO.read(r"C:\ReadMyCourse\PFB_practice\drug developement pipelines\sample_file_small.aln", "clustal")
# print(alignment)

import matplotlib.pylab as plt
from Bio import Phylo
tree = Phylo.read(r"C:\ReadMyCourse\PFB_practice\drug developement pipelines\sample_file_small.dnd", "newick")
#Phylo.draw_ascii(tree) #draw on commandline
Phylo.draw(tree, branch_labels=lambda c: c.branch_length) #plot with branch length
plt.savefig("temp")
#Phylo.draw(tree) #to draw like plot