#' This script is used to extract the gene matrix based on the single cell barcode list
#'

import os
import re
import sys


feature=open(sys.argv[1],'r')#Single cell barcode list
TrEx1=open(sys.argv[2],'r')#scRNA-Seq matrix
TrEx2=open(sys.argv[2],'r')#scRNA-Seq matrix
predD=open(sys.argv[3],'w')#ouput of matrix data


mkl=[]
mkls={}


for line in feature:
    line=line.strip()
    line=line.split()
    mkl.append(line[0])
    mkls[line[0]]=line[0]


nte=[]

for line in TrEx1:
    line=line.strip()
    lineE=line.split()
    a=0
    if '"' in lineE[1]:
        for n in range(0,int(len(lineE))):
                a=a+1
                if lineE[n] in mkls:
                    nte.append(a)


#getting the expression of features
cellID=''
exp=''

for line in TrEx2:
    line=line.strip()
    lineE=line.split()
    if '"' in lineE[1]:
        for id in range(0,int(len(lineE))):
            if lineE[id] in mkls.keys():
                cellID=cellID+lineE[id]+'       '
        print >>predD,cellID
        cellID

    if '"' not in lineE[1]:
        
        for value in nte:
            #print value,len(lineE)
            exp=exp+lineE[int(value)]+' '
        
        print >>predD,lineE[0]+'        '+exp
        exp=''
        

feature.close()
TrEx1.close()
TrEx2.close()
predD.close()

