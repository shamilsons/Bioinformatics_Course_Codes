# -*- coding: utf-8 -*-

from string import *
from random import *
#from os import *
from math import *
from time import time
from datetime import datetime

'''
=== ALGORITHMS TO IMPLEMENT ===================================================================
https://gist.github.com/shamilsons/673517f68e1e4150c2d6ac620beac4d8
1. Generating DNA-RNA-Protein Sequences (with probability functions)
2. Calculating
    - GC% contents (download sequences from NCBI-Genbank and perform analysis)
    - di and tri nucleotide statistics, http://www.genomatix.de/cgi-bin/tools/tools.pl
    - complement and reverse complement
3. Finding regulatory regions
    - Start, stop, Tata-boxes (TATAAT, TATAAA) etc. in prokaryotes and eukaryotes
    - In Bacteria (https://en.wikipedia.org/wiki/Promoter_(genetics))
    - Eukaryotes (https://www.ncbi.nlm.nih.gov/books/NBK21745/)
4. Transcription and Translation process
    - based on six frameshifts
5. Finding gene coding regions
    - find overlapping genes and protein sequences
6. Exon-intron protein sequence translations (find most suitable sequences)
7. ORC problem
8. Fiding most frequent appearing sub-sequences
9. Motif Finding
10. PSA algorithm for dna and protein sequence
11. BioPython framework implementations
12. Organize program in packages(modules)
================================================================================================
'''
#Hold DNA nucleotides
dnaNucs=('A','T','G','C')
#Hold RNA nucleotides
rnaNucs=('A','U','G','C')
#Hold Protein aminoacids
prtnAA=('R','Q','F','Y', 'W', 'L', 'G', 'A', 'H', 'S', 'P', 'E', 'D', 'T', 'C', 'M', 'L', 'N', 'I', 'V')

#1st solution
#DNA and RNA start and stop codons codes
start_codons=('ATG', 'TTG','CTG')
stop_codon=('TAA','TAG','TGA')
rna_start_codons=('AUG', 'UUG','CUG')
rna_stop_codon=('UAA','UAG','UGA')

#Amino acid Dna Codons
pheDnaCodons=('TTT','TTC')
leuDnaCodons=('TTA','TTG','CTT','CTC','CTA','CTG')
ileDnaCodons=('ATT','ATC','ATA')
metDnaCodons=('ATG')
valDnaCodons=('GTT','GTC','GTA','GTG')
serDnaCodons=('TCT','TCC','TCA','TCG','AGT','AGC')
proDnaCodons=('CCT','CCC','CCA','CCG')
thrDnaCodons=('ACT','ACC','ACA','ACG')
alaDnaCodons=('GCT','GCC','GCA','GCG')
tyrDnaCodons=('TAT','TAC')
hisDnaCodons=('CAT','CAC')
glnDnaCodons=('CAA','CAG')
asnDnaCodons=('AAT','AAC')
lysDnaCodons=('AAA','AAG')
aspDnaCodons=('GAT','GAC')
gluDnaCodons=('GAA','GAG')
cysDnaCodons=('TGT','TGC')
trpDnaCodons=('TGG')
argDnaCodons=('CGT','CGC','CGA','GGG','AGA','AGG')
glyDnaCodons=('GGT','GGC','GGA','GGG')

#Amino acid hash tables
aminoAcidHashTableSingleLettered={'F':'Phenylalanine', 'L':'Leucine', 'I':'Isoleucine', 'M':'Methionine','V':'Valine', 'S':'Serine', 'P':'Proline', 'T':'Threonine', 'A':'Alanine', 'Y':'Tyrosine', 'H':'Histidine','Q':'Glutamine','N':'Asparagine','K':'Lysine','D':'Aspartic acid','E':'Glutamic acid','C':'Cystine','W':'Tryptophan','R':'Arginine','G':'Glycine'}
aminoAcidHashTableTripleLettered={'Phe':'Phenylalanine', 'Leu':'Leucine', 'Ile':'Isoleucine', 'Met':'Methionine','Val':'Valine', 'Ser':'Serine', 'Pro':'Proline', 'Thr':'Threonine', 'Ala':'Alanine', 'Tyr':'Tyrosine', 'His':'Histidine','Gln':'Glutamine','Asn':'Asparagine','Lys':'Lysine','Asp':'Aspartic acid','Glu':'Glutamic acid','Cys':'Cystine','Trp':'Tryptophan','Arg':'Arginine','Gly':'Glycine'}
aminoAcidHashTableToCodonSingle11={'F':pheDnaCodons, 'L':leuDnaCodons, 'I':ileDnaCodons, 'M':metDnaCodons,'V':valDnaCodons, 'S':serDnaCodons, 'P':proDnaCodons, 'T':thrDnaCodons, 'A':alaDnaCodons, 'Y':tyrDnaCodons, 'H':hisDnaCodons,'Q':glnDnaCodons,'N':asnDnaCodons,'K':lysDnaCodons,'D':aspDnaCodons,'E':gluDnaCodons,'C':cysDnaCodons,'W':trpDnaCodons,'R':argDnaCodons,'G':glyDnaCodons}
aminoAcidHashTableToCodonTriple12={'Phe':pheDnaCodons, 'Leu':leuDnaCodons, 'Ile':ileDnaCodons, 'Met':metDnaCodons,'Val':valDnaCodons, 'Ser':serDnaCodons, 'Pro':proDnaCodons, 'Thr':thrDnaCodons, 'Ala':alaDnaCodons, 'Tyr':tyrDnaCodons, 'His':hisDnaCodons,'Gln':glnDnaCodons,'Asn':asnDnaCodons,'Lys':lysDnaCodons,'Asp':aspDnaCodons,'Glu':gluDnaCodons,'Cys':cysDnaCodons,'Trp':trpDnaCodons,'Arg':argDnaCodons,'Gly':glyDnaCodons}

#2nd solution
aminoAcidHashTableToCodonSingle21 = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
}

def generateSequence(type='dna', seqLen=100, pdf=[0.15,0.15,0.35,0.35]):
    sequence=[]
    '''
    for i in range(0,seqLen,1):
        sequence.append('0')
    print 'Initial length:', len(sequence)
    #for cnt in range(0,seqLen-1,1):
    for nuc in range(1,15,1):
        idx = randint(0, seqLen-1)
        if(sequence[idx]=='0'):
            sequence[idx]='A'
    for nuc in range(1,20,1):
        idx = randint(0, seqLen-1)
        if(sequence[idx]=='0'):
            sequence[idx]='T'
    for nuc in range(1,30,1):
        idx = randint(0, seqLen-1)
        if(sequence[idx]=='0'):
            sequence[idx] ='G'
    for nuc in range(1,35,1):
        idx = randint(0, seqLen-1)
        if(sequence[idx]=='0'):
            sequence[idx]='C'
    return join(sequence,'')
    '''
    cntA = seqLen * pdf[0]
    cntT = seqLen * pdf[1]
    cntG = seqLen * pdf[2]
    cntC = seqLen * pdf[3]

    if(type=='dna'):
        while seqLen>0:
            nucRange = randint(1, 100)
            if(nucRange>=1 and nucRange<=15 and cntA!=0):
                sequence.append('A')
                cntA-=1
            elif(nucRange>=16 and nucRange<=40 and cntT!=0):
                sequence.append('T')
                cntT-=1
            elif(nucRange>=41 and nucRange<=90 and cntG!=0):
                sequence.append('G')
                cntG-=1
            else:
                sequence.append('C')
                cntC-= 1
            seqLen-=1

        return join(sequence,'')

def menu(type='main'):
    if(type=='main'):
        print '== MENU =='
        print '1. Generate sequence'
        print '2. NT% statistics'
        print '3. di-nuc and tri-nuc statistics'
        print '4. EXIT'
'''
def seqComposition(seq='',shift=1):
    seqComp={}
    cnt=0
    while cnt<=len(seq)-(shift):
        key=seq[cnt:cnt+shift]
        if(seqComp.has_key(key)):
            seqComp[key]+=1/float(len(seq)-(shift-1))
        else:
            seqComp[key]=1/float(len(seq)-(shift-1))
        cnt+=1
        print cnt,'.',key
    print seqComp
#print seqComposition('ATGTTCGGTCGTGA',1)
'''
def sequenceOperations(seq,optType):
    sequence=[]
    counter=len(seq)-1
    if(optType=='revComp'):
        #print 'Calisiyor'+str(counter)
        while counter>-1:
            if(seq[counter]=='A'):
                sequence.append('T')
            elif(seq[counter]=='T'):
                sequence.append('A')
            elif(seq[counter]=='G'):
                sequence.append('C')
            else:
                sequence.append('G')
            counter=counter-1

    return join(sequence,'')

#Non-Recursive algorithm to get the codons of an entered sequence
def getSeqCodons(sequence,pos):
    codons=[]
    counter=0
    start_slice=pos-1 #translates to +1 +2 +3, -1,-2,-3
    stop_slice=start_slice+3

    if(pos<0):
        start_slice=-1*(pos)-1 #translates to +1 +2 +3, -1,-2,-3
        stop_slice=start_slice+3
        sequence=sequenceOperations(sequence,'revComp')

    while counter<len(sequence):
        if(sequence[start_slice:stop_slice]!=''):
            if(len(sequence[start_slice:stop_slice])==3):
                codons.append(sequence[start_slice:stop_slice])
            start_slice=stop_slice
            stop_slice=stop_slice+3
        else:
            break
        counter+=1

    return codons

#Function that translates DNA sequence to Protein needs a getSeqCodons function
def translationProcess1(seq,pos):
    counter=0
    protein=[]
    seqcodons=getSeqCodons(seq,pos)
    while counter<len(seqcodons):
        for key,codonset in aminoAcidHashTableToCodonSingle11.items():
            if(seqcodons[counter] in codonset):
                protein.append(key)
                break
        counter=counter+1
    return join(protein,'')

def translationProcess2(seqDNA, startReg, stopReg, dnaStrand):
    if((startReg-stopReg)<90):
        return 'Cannot perform translation operation must be at least 90bp'

    proteinSeq = ''
    seqDNA=seqDNA[startReg:stopReg]
    if(dnaStrand=='+'):
        for idx in range(0,len(seqDNA),3):
            codon = seqDNA[idx:idx + 3]
            proteinSeq = proteinSeq + aminoAcidHashTableToCodonSingle21[codon]
        return proteinSeq
    else:
        seqDNA=sequenceOperations(seqDNA,'revComp')
        for idx in range(0,len(seqDNA),3):
            codon = seqDNA[idx:idx + 3]
            proteinSeq = proteinSeq + aminoAcidHashTableToCodonSingle21[codon]
        return proteinSeq

def readSeqFromFile(filename):
    #f1=open('dutPasebacteria.txt','r')
    #f2=open('dutPasehuman.txt','r')
    seqFile = open(filename, 'r')
    cnt = 0
    seq = []
    for line in seqFile:
        if (line[0] != '>'):
            line = line.rstrip()
            # print cnt,'.',line
            seq.append(line)
            cnt += 1
    return join(seq,'')

filename='dutPasebacteria.txt'
#readSeqFromFile(filename)[343:798]

t0 = datetime.now()
print 'Translation process of 1st is:', translationProcess1(readSeqFromFile(filename)[342:798],1)
t1 = datetime.now()
print 'Translation process of 2st is:', translationProcess2(readSeqFromFile(filename),342,798,'+')
t2 = datetime.now()

print 'Translation process 1 function takes:',(t1-t0).microseconds, 'microseconds'
print 'Translation process 2 function takes:',(t2-t1).microseconds, 'microseconds'

print sequenceOperations('TATATG','revComp')

'''
def main():
    checkMenu=True
    menu('main')
    while(checkMenu):
        option = input('Please select option:')
        if(option==1):
            seqTarget=generateSequence('dna',100,[0.1,0.4,0.4,0.1])
            print 'Target sequence:',seqTarget
            print 'Len sequence:',len(seqTarget)
            print 'A:',count(seqTarget,'A'),' T:',count(seqTarget,'T'),' G',count(seqTarget,'G'),' C',count(seqTarget,'C')
        elif(option==2):
            print 'bla bla bla 2'
            print '\n' * 100
        elif (option == 3):
            print 'bla bla bla 3'
            print '\n' * 100
        else:
            checkMenu=False
main()
'''
