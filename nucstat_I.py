from string import *
from random import *

#DNA nucleotides defined in tuple
dna_nuc=('A','T','G','C')

#Store generated tri-nucleotide sequences
nuc_lst=[]
nuc_sts={'ATG':0,'TAA':0}

def main():
    counter=0
    check=True
    while counter<=200:
        seqDNA=dna_nuc[randint(0,3)]+dna_nuc[randint(0,3)]+dna_nuc[randint(0,3)]
        nuc_lst.append(seqDNA)
        if(seqDNA=='ATG'):
            nuc_sts['ATG']=nuc_sts['ATG']+1
        elif(seqDNA=='TAA'):
            nuc_sts['TAA']=nuc_sts['TAA']+1

        if(nuc_sts['ATG']>3 and nuc_sts['TAA']>2):
            check=False
            break
        else:
            print counter
            continue

        counter=counter+1

    if(check):
        print 'Program executed without intervention'
    else:
        print 'Stopped by condition'

    print nuc_sts

main()
