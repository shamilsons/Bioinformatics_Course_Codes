#FUGENE version 1.1 program

from string import *
from random import *

#DNA and RNA nucleotides defined in tuple
dna_nuc=('A','T','G','C')
rna_nuc=('A','U','G','C')

#DNA and RNA start and stop codons codes
start_codons=('ATG')
stop_codon=('TAA','TAG','TGA')
rna_start_codons=('AUG')
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
aminoAcidHashTableToCodonSingle={'F':pheDnaCodons, 'L':leuDnaCodons, 'I':ileDnaCodons, 'M':metDnaCodons,'V':valDnaCodons, 'S':serDnaCodons, 'P':proDnaCodons, 'T':thrDnaCodons, 'A':alaDnaCodons, 'Y':tyrDnaCodons, 'H':hisDnaCodons,'Q':glnDnaCodons,'N':asnDnaCodons,'K':lysDnaCodons,'D':aspDnaCodons,'E':gluDnaCodons,'C':cysDnaCodons,'W':trpDnaCodons,'R':argDnaCodons,'G':glyDnaCodons}
aminoAcidHashTableToCodonTriple={'Phe':pheDnaCodons, 'Leu':leuDnaCodons, 'Ile':ileDnaCodons, 'Met':metDnaCodons,'Val':valDnaCodons, 'Ser':serDnaCodons, 'Pro':proDnaCodons, 'Thr':thrDnaCodons, 'Ala':alaDnaCodons, 'Tyr':tyrDnaCodons, 'His':hisDnaCodons,'Gln':glnDnaCodons,'Asn':asnDnaCodons,'Lys':lysDnaCodons,'Asp':aspDnaCodons,'Glu':gluDnaCodons,'Cys':cysDnaCodons,'Trp':trpDnaCodons,'Arg':argDnaCodons,'Gly':glyDnaCodons}

#Amino acid definitions
aminoAcidSingleCodes=aminoAcidHashTableSingleLettered.keys()
aminoAcidTripleCodes=aminoAcidHashTableTripleLettered.keys()

#Non-Recursive algorithm to get the codons of an entered sequence
def getSeqCodons(sequence,pos):
    counter=0
    start_slice=pos #0,1,2 translates to +1 +2 +3
    stop_slice=start_slice+3
    codons=[]
    while counter<len(sequence):
        if(sequence[start_slice:stop_slice]!=''):
            codons.append(sequence[start_slice:stop_slice])
            start_slice,stop_slice=stop_slice,stop_slice+3
        else:
            break
        counter+=1
    return codons

#Function that translates DNA sequence to Protein needs a getSeqCodons function
def translateDNAtoProtein(seq,pos):
    counter=0
    protein=[]
    seqcodons=getSeqCodons(seq,pos)
    while counter<len(seqcodons):
        for key,codonset in aminoAcidHashTableToCodonSingle.items():
            if(seqcodons[counter] in codonset):
                protein.append(key)
                break
        counter=counter+1
    return join(protein,'')
    
def genSequence(seqType=0,seqLen=3):
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
        print 'Protein sequence'
    #Generates RNA sequence
    else:
        while counter<seqLen:
            product.append(rna_nuc[randint(0,3)])
            counter=counter+1
        return product

def storeSequences():
    seqFile=open('seqDNA.txt',"w")
    print "File has been created ..."
    counter=0
    while counter<10:
        seqFile.write(join(genSequence(0,10),'')+'\n')
        counter+=1
    seqFile.close()
    print 'DNA Sequences created file closed'

def readSequences():
    seqFile=open('seqDNA.txt',"r")
    print 'File opened for reading'
    sequences=seqFile.readlines()
    count=1
    for sequence in sequences:
        print str(count)+'.'+sequence.strip()
        count+=1
    seqFile.close()

def calculateGC(sequence):
    dataGC={'C':0,'G':0}
    for nucleotide in sequence:
        if(nucleotide=='C'):
            dataGC['C']+=1
        elif(nucleotide=='G'):
            dataGC['G']+=1
        else:
            continue
    print 'GC%:'+str((float((dataGC['C']+dataGC['G']))/len(sequence))*100)

def getSeqCodons(sequence):
    counter=0
    start_slice=0 #0,1,2 translates to +1 +2 +3
    stop_slice=3
    codons=[]
    while counter<len(sequence)/3+1:
        if(sequence[start_slice:stop_slice]!=''):
            codons.append(join(sequence[start_slice:stop_slice],''))
            start_slice=stop_slice
            stop_slice=stop_slice+3
        else:
            break
        counter+=1
    return codons
    
    
#Write a simple algorithm that will check whether the
#entered sequence is DNA,RNA or Protein and return type
def checkSequence(sequence):
    print 'Code to check whether the sequence is DNA, RNA or Protein'
    

def menu_contents():
    menu={0:'== MENU ==',1:'Generate sequence',2:'Display sequence',3:'Calculate GC%',4:'Store sequences',5:'Read stored sequences',6:'Get DNA codons',7:'EXIT'}
    keys=menu.keys()
    for i in range(0,len(keys)):
        if(i==0):
            print menu[keys[i]]
        else:
            print str(keys[i])+'.'+menu[keys[i]]

def main():
    lcon=True
    sequence=''

    while lcon:
        menu_contents()
        #perform type casting
        option=int(raw_input('Enter option:'))

        if(option==1):
            print '\n'*20
            seqType=input('Type of a sequence(0-DNA,1-Protein,2-RNA)')
            seqLen=input('Enter sequence length')
            sequence=genSequence(seqType,seqLen)
            print 'Sequence generated'
        elif(option==2):
            print '\n'*20
            print 'Sequence:'+join(sequence,'')
        elif(option==3):
            print '\n'*20
            calculateGC(sequence)
        elif(option==4):
            print '\n'*20
            storeSequences()
        elif(option==5):
            print '\n'*20
            readSequences()
        elif(option==6):
            print '\n'*20
            print getSeqCodons(sequence)
        else:
            lcon=False

main()
