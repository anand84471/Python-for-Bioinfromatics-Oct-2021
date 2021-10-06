seq="ATGCATGCA"

#  0    1    2    3    4    5    6    7    8      left-right 
#  ↓    ↓    ↓    ↓    ↓    ↓    ↓    ↓    ↓
# ['A', 'T', 'G', 'C', 'A', 'T', 'G', 'C', 'A']
#  ↑    ↑    ↑    ↑    ↑    ↑    ↑    ↑    ↑
# -9   -8   -7   -6   -5   -4   -3   -2   -1      right-left

#left to right indexing
print(seq[0])
print(seq[2])


#right to left indexing
print(seq[-1])
print(seq[-3])
print(seq[-4])

#program to find the base present in the 3rd position
print(seq[2])

#program to find out the base present at the third last postion
print(seq[-3])