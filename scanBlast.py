#!/bin/usr/ python3
import sys
input=sys.argv[1]
#For exon
#name=input.split('_')
#prefix=name[0]
#middle=name[1].split('-')
#middlename=middle[0]
#strain=middle[1]
#

#For tf
name=input.split('_')
prefix=name[0]
middlename=name[1]
strain=name[2]
#


f=open(input,'r').readlines()
clean=[]
All=[]

#Transfer blt file into list with original lines order
for i in f:
    x=i.rstrip('\n').split(' ')
    for z in x:
        if z != '':
            clean.append(z)
    All.append(clean)
    clean=[]
#print(All)


#The even number is for subject, and the odd number is for query 
subjectSeq=[]
querySeq=[]
pairCoor={}
for i in All:
    if All.index(i)%2==0:
        querySeq.append(i)
    else:
        subjectSeq.append(i)

for i in range(0,len(querySeq)):
    pairCoor[subjectSeq[i][0]]=querySeq[i][0]

queryDict={}
for i in querySeq:
    queryDict[i[0]]=i[1]
#print(queryDict)
#print(querySeq)
#print(pairCoor)


#Scanning mutation and its position
mutation=[]
count=-1
for read in subjectSeq:
    for nt in read[1]:
        if count <59:
            count+=1
        else:
            count=0
        if nt != '.':
            info=str(read[0])+'\t'+str(nt)+'\t'+str(count)
            mutation.append(info)
    count=-1
#print(mutation)

#extract query nt
for i in mutation:
    line=i.split('\t')
    subjectidx=line[0]
    subjectnt=line[1]
    position=line[2]
    queryidx=pairCoor[subjectidx]
    querynt=queryDict[queryidx][int(position)]
#    mutpos=int(subjectidx)+int(position)
    mutpos=int(subjectidx)-int(position)
    final=str(mutpos)+'\t'+str(subjectnt)+'\t'+str(querynt)
    if querynt == '-':
        print(prefix+'\t'+middlename+'\t'+strain+'\t'+final+'\t'+'deletion')
    elif subjectnt == '-':
        print(prefix+'\t'+middlename+'\t'+strain+'\t'+final+'\t'+'insertion')
    else:
        print(prefix+'\t'+middlename+'\t'+strain+'\t'+final+'\t'+'substitution')







