seq="ATAGTA"
length_seq=len(seq)
#syntax
if length_seq>10:
    print("The length of the sequence is greater than 10 ")
else:
    print("The length of the sequence is less than 10 ")


epitope="VEKGVLPQLEQ"

if len(epitope)>10:
    print("This is an ideal epitope")
else:
    print("This is not an ideal epitope")





"""
A: >=90
B: >=80 <90
C: <80
"""
seq=input("Please enter the seq: ")
gc_percentage=100*(seq.count("G")+seq.count("C"))/len(seq)
print(gc_percentage)
if gc_percentage>=90:
    print("A")
elif gc_percentage>=80 and gc_percentage<90:
    print("B")
else:
    print("C")





"""
A: >=90
   IF length>10:
       This is an ideal seq
B: >=80 <90
C: <80
"""
seq=input("Please enter the seq: ")
gc_percentage=100*(seq.count("G")+seq.count("C"))/len(seq)
print(gc_percentage)
if gc_percentage>=90:
    if len(seq)>10:
        print("This is an ideal seq")
    print("A")
elif gc_percentage>=80 and gc_percentage<90:
    print("B")
else:
    print("C")