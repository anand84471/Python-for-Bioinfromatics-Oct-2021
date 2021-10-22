# Q1. Write a program to find the second maximum GC value from the list also find the median GC value.
#     Gc values are as follows 30.5,12,54,23,84
# Answer
list1=[30.5, 12, 54, 23, 84]
list1.sort()
list1.reverse()

print(list1)
print(list1[1])
length=int(len(list1))
print(length)
if int(length)%2!=0 :
    median_odd=int((length+1)/2)
    print("The list contain odd no of value and median of the list is ", list1[median_odd-1])
else:
    median_1=int(length/2)
    median_2=int(length/2+1)
    median_even=float(int(list1[median_1-1])+int(list1[median_2-1]))/2
    print("The list contain the even no of items and median of the list is ", median_even)


# Q2. Write a program to check which stop codons are present in the sequence  â€œUAAAAGGCGAGAUAAAUAâ€.
#Answer
rna_seq="UAAAAGGCGAGAUAAAUA"  
print("There are 3 stop codons are present UAA, UGA and UAG and their presence in this (UAAAAGGCGAGAUAAAUA) sequence")
print("The presence of UAA in sequence is", "UAA" in rna_seq)
print("The presence of UGA in sequence is", "UGA" in rna_seq)
print("The presence of UAG in sequence is",  "UAG" in rna_seq)



# Q3. Check the presence of all the stop codons in the list ["UAA","UGC","AUAGCT","ATUA","UAG"].

list2=["UAA","UGC","AUAGCT","ATUA","UAG"]
stop_codon_1="UAA" # this is stop codon 1
stop_codon_2="UGA"
stop_codon_3="UAG"
for stop_codon in list2:
 if stop_codon.count(stop_codon_1)>0 :
  print("There is", stop_codon.count(stop_codon_1), "of UAA in",  stop_codon)
 elif stop_codon.count(stop_codon_2)>0:
  print("There is", stop_codon.count(stop_codon_2), "of UGA in",  stop_codon)
 elif stop_codon.count(stop_codon_3)>0:
  print("There is", stop_codon.count(stop_codon_3), "of UAG in", stop_codon)
 else:
    print("There is no stop codon in", stop_codon)


# Q4. Write a program to transcribe the sequence "ATGCTCGCGTAA"
#Answer
# DNA sequence is "ATGCTCGCGTAA" and transcription is this sequence into mRNA. haivng U instead of T.
list3=["ATGCTCGCGTAA"]
list3=str(list3)
list_a=list3.replace("T","U")



print("The transcribe sequence of 'ATGCTCGCGTAA' sequence is",list_a)


# Q5. Concatenate two lists of GC Values [30.5,12,54,23,84] and [12,45,54,32] 
#     and find the maxium and minum GC Values. 
list4=[30.5,12,54,23,84]
list5=[12,45,54,32]
list_new=list4+list5
print(list_new)
list_new.sort()
print(list_new)
print("The mimimum GC value is", list_new[0],"The maximum GC value is ", list_new[-1]," in the list", list_new)