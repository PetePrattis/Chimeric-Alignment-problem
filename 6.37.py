import sys
import random
'''
cdna =[]
x=0
n=['A', 'C', 'G', 'T']
y = random.randrange(1, 50)
while x < y:
    rdna = random.choice(n)
    for i in range(0, random.randrange(1, y/4)):
        cdna.append(rdna)
        x= len(cdna)
'''

corrupteddna="AAATAAAGGGGCCCCCTTTTTTTCC"
cdna = list(corrupteddna)
        
dna=[]
for i in range(len(cdna)):
    print cdna[i],

print    
replays=1
for i in range(1, len(cdna)):
    if cdna[0] != cdna[1] and i==1:
        dna.append(cdna[0])
    elif cdna[i-1] == cdna[i] and cdna[i]=="A" and replays <5 and i!=len(cdna)-1:
        replays= replays+ 1
    elif cdna[i-1] == cdna[i] and cdna[i]=="A" and replays ==5 and i!=len(cdna)-1:
        add = random.randrange(1,replays)
        for j in range(add): 
            dna.append('A')
        replays=1
    elif cdna[i-1] == cdna[i] and cdna[i]=="C" and replays <10 and i!=len(cdna)-1:
        replays= replays+ 1
    elif cdna[i-1] == cdna[i] and cdna[i]=="C" and replays ==10 and i!=len(cdna)-1:
        add = random.randrange(1,replays)
        for j in range(add): 
            dna.append('C')
        replays=1
    elif cdna[i-1] == cdna[i] and cdna[i]=="G" and i!=len(cdna)-1:
        replays= replays+ 1
    elif cdna[i-1] == cdna[i] and cdna[i]=="T" and i!=len(cdna)-1:
        replays= replays+ 1
    elif cdna[i] != cdna[i-1] and i!=len(cdna)-1:
        if replays > 1:
            add = random.randrange(1,replays)
            for j in range(add): 
                dna.append(cdna[i-1])
        elif replays ==1:
            dna.append(cdna[i-1])
        replays=1
    elif i==len(cdna)-1:
        dna.append(cdna[i])

for i in range(len(dna)):
    print dna[i],
    
print
