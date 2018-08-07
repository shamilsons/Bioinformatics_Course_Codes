#FUGENE version 1.13 program

from string import *
from random import *
from math import *

#DNA and RNA nucleotides defined in tuple
dna_nuc=('A','T','G','C')

#SeqType 0:DNA, 1:RNA, 2:Protein
def genSequence(seqLen=50, seqType=0):
    counter=0
    product=[]
    #Generates DNA sequence
    if(seqType==0):
        while counter<seqLen:
            product.append(dna_nuc[randint(0,3)])
            counter=counter+1
        return product
    #Generates Protein sequence
    elif(seqType==1):
        while counter<seqLen:
            product.append(rna_nuc[randint(0,3)])
            counter=counter+1
        return product
    #Generates RNA sequence
    else:
        print 'Protein sequence'

def genSequenceDP(seqLen, seqType, pd):
    counter=0
    product=[]

    num_a=int(round(seqLen*pd[0]))
    num_t=int(round(seqLen*pd[1]))
    num_g=int(round(seqLen*pd[2]))
    num_c=int(round(seqLen*pd[3]))

    """
    if((seqLen*pd[0]-int(seqLen*pd[0]))>0.5):
        num_a=int(ceil(seqLen*pd[0]))
    else:
        num_a=int(floor(seqLen*pd[0]))
    if((seqLen*pd[1]-int(seqLen*pd[1]))>0.5):
        num_t=int(ceil(seqLen*pd[1]))
    else:
        num_t=int(floor(seqLen*pd[1]))
    if((seqLen*pd[2]-int(seqLen*pd[2]))>0.5):
        num_g=int(ceil(seqLen*pd[2]))
    else:
        num_g=int(floor(seqLen*pd[2]))
    if((seqLen*pd[3]-int(seqLen*pd[3]))>0.5):
        num_c=int(ceil(seqLen*pd[3]))
    else:
        num_c=int(floor(seqLen*pd[3]))
    """

    print "Nucleotide sets before generating sequence"
    print "A nuc set:%d"%(num_a)
    print "T nuc set:%d"%(num_t)
    print "G nuc set:%d"%(num_g)
    print "C nuc set:%d"%(num_c)

    while counter<seqLen:
        slp=randint(1,100)
        if((slp>=1 and slp<=40) and num_a!=0):
            product.append('A')
            num_a=num_a-1
        elif((slp>=41 and slp<=80) and num_t!=0):
            product.append('T')
            num_t=num_t-1
        elif((slp>=81 and slp<=90) and num_g!=0):
            product.append('G')
            num_g=num_g-1
        elif((slp>=91 and slp<=100) and num_c!=0):
            product.append('C')
            num_c=num_c-1

        #print "Counter:"+str(counter)
        counter+=1

    print "Nucleotide sets after generating sequence"
    print "A nuc set:%d"%(num_a)
    print "T nuc set:%d"%(num_t)
    print "G nuc set:%d"%(num_g)
    print "C nuc set:%d"%(num_c)

    return product

def dna_stats(seqDna, step_size=1, stat_tp=1):
    counter=0
    print join(seqDna, '')
    stat_table={}

    while counter<len(seqDna)-(stat_tp-1):
        key=join(seqDna[counter:counter+stat_tp],'')
        if(stat_table.has_key(key)):
            stat_table[key]=stat_table[key]+1
        else:
            stat_table[key]=1
        counter=counter+step_size

    if(stat_table.has_key('TATA')):
        print "TATA box number:%d"%stat_table['TATA']
    else:
        print 'No TATA boxes haha ...'
    print stat_table

# Below is the hint for function execution
# k_mers(seqTemp,5,10)
def k_mers(seqDna, kmers, cutoff):
    counter=0
    step_size=1
    stat_table={}

    while counter<len(seqDna)-(kmers-1):
        key=join(seqDna[counter:counter+kmers],'')
        if(stat_table.has_key(key)):
            loc=stat_table[key][1]
            loc.append(counter)
            stat_table[key]=[[stat_table[key][0][0]+1],loc]
        else:
            stat_table[key]=[[1],[counter]]

        counter=counter+step_size

    for key in stat_table:
        if(stat_table[key][0]>=cutoff):
            print key," ",stat_table[key]

def main():
    seqDna=join(genSequenceDP(100,0,(0.40, 0.40, 0.10, 0.10)),'')
    #print join(seqDna, '')
    dna_stats(seqDna,1,4)

    print "Number of TATA boxes:%d"%(seqDna.count('TATA'))
    #print len(seqDNA)

    print "File is being opened for reading"

    seqfile=open("dnaDB.fasta", "rb")
    seqTemp=seqfile.read()
    seqTemp=seqTemp.replace("\n","") #removing new lines symbols
    seqTemp=seqTemp.replace("\r","") #removing carrot symbols
    seqfile.close()

    print "Sequence length:",len(seqTemp),"bp"
    k_mers(seqTemp,5,10)

main()
