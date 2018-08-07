from random import *
from string import *

#DNA nucleotidleri tutuyor
dnaNucs=('A','T','G','C')
rnaNucs=('A','U','G','C')
prtnAA=('R','Q','F','Y', 'W', 'L', 'G', 'A', 'H', 'S', 'P', 'E', 'D', 'T', 'C', 'M', 'L', 'N', 'I', 'V')

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
aminoAcidHashTableToCodonSingle={'F':pheDnaCodons, 'L':leuDnaCodons, 'I':ileDnaCodons, 'M':metDnaCodons,'V':valDnaCodons, 'S':serDnaCodons, 'P':proDnaCodons, 'T':thrDnaCodons, 'A':alaDnaCodons, 'Y':tyrDnaCodons, 'H':hisDnaCodons,'Q':glnDnaCodons,'N':asnDnaCodons,'K':lysDnaCodons,'D':aspDnaCodons,'E':gluDnaCodons,'C':cysDnaCodons,'W':trpDnaCodons,'R':argDnaCodons,'G':glyDnaCodons}
aminoAcidHashTableToCodonTriple={'Phe':pheDnaCodons, 'Leu':leuDnaCodons, 'Ile':ileDnaCodons, 'Met':metDnaCodons,'Val':valDnaCodons, 'Ser':serDnaCodons, 'Pro':proDnaCodons, 'Thr':thrDnaCodons, 'Ala':alaDnaCodons, 'Tyr':tyrDnaCodons, 'His':hisDnaCodons,'Gln':glnDnaCodons,'Asn':asnDnaCodons,'Lys':lysDnaCodons,'Asp':aspDnaCodons,'Glu':gluDnaCodons,'Cys':cysDnaCodons,'Trp':trpDnaCodons,'Arg':argDnaCodons,'Gly':glyDnaCodons}

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
    return protein

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


#Hemoglobin statistics
#A:0.20 T:0.24 G:0.30 C:0.26 - Hemoglobin ailesi icin pdf statistigi
#pdf=(0.20,0.24,0.30,0.26)
def generateSequencePDF(tip,ln,pdf):
    output=[]
    counter=0

    #nucleotide Bucket
    nuc_A=int((ln*pdf[0]))
    print "nuc_A:"+str(nuc_A)
    nuc_T=int((ln*pdf[1]))
    print "nuc_T:"+str(nuc_T)
    nuc_G=int((ln*pdf[2]))
    print "nuc_G:"+str(nuc_G)
    nuc_C=int((ln*pdf[3]))
    print "nuc_C:"+str(nuc_C)

    nuc_Total=nuc_A+nuc_T+nuc_G+nuc_C

    if(tip=='DNA' or tip=='RNA'):
        while counter<nuc_Total:
            #selector
            slc_prb=randint(1,10)
            if((slc_prb>=1 and slc_prb<=3) and nuc_A!=0):
                output.append('A')
                nuc_A=nuc_A-1
            elif((slc_prb>=4 and slc_prb<=5) and nuc_T!=0):
                output.append('T')
                nuc_T=nuc_T-1
            elif((slc_prb>=6 and slc_prb<=8) and nuc_G!=0):
                output.append('G')
                nuc_G=nuc_G-1
            elif((slc_prb>=9 and slc_prb<=10) and nuc_C!=0):
                output.append('C')
                nuc_C=nuc_C-1
            else:
                continue

            counter=counter+1

        return join(output,'')
    else:
        output='Not working for protein sequences'
        return output

def addDetails(sequence):
    #helix1='VDEVGGEALGRLLVV'   #21-35 ->15aa
    #helix2='PKVKAHGKKVLGAFSDG' #59-75 -> 17aa
    #helix3='PPVQAAYQKVVAGVANALA' #125-143 -> 19aa
    helix=('VDEVGGEALGRLLVV','PKVKAHGKKVLGAFSDG','PPVQAAYQKVVAGVANALA')
    uturn='HLD' #78-80 ->3aa

    protein=join(translateDNAtoProtein(sequence,1),'')

    counter=randint(1,3)
    print '\nNumber of helixes to add:'+str(counter)+'\n'
    while counter>0:
        slc_helix=randint(0,2)
        add_index=randint(0,len(protein)-1)
        print 'Selected helix:'+str(slc_helix)+' index:'+str(add_index)
        protein=protein[:add_index] + helix[slc_helix] + protein[add_index:]
        counter=counter-1

    #uturn
    add_index=randint(0,len(protein)-1)
    print '\nUturn index:'+str(add_index)
    protein=protein[:add_index] + uturn + protein[add_index:]

    return protein

def generateSequence(tip,ln):
    output=[]
    counter=0

    if(tip=='dna'):
        while counter<ln:
            output.append(dnaNucs[randint(0,3)])
            counter+=1 # counter=counter+1
        return join(output,'')
    elif(tip=='rna'):
        while counter<ln:
            output.append(rnaNucs[randint(0,3)])
            counter+=1 # counter=counter+1
        return join(output,'')
    else:
        while counter<ln:
            output.append(prtnAA[randint(0,19)])
            counter+=1 # counter=counter+1
        return join(output,'')

def atgcPercent(sequence):
    nuc_a=0
    nuc_t=0
    nuc_g=0
    nuc_c=0
    #nuc_n=0
    sequence=lower(sequence)
    for nuc in sequence:
        if(nuc=='a'):
            nuc_a+=1
        elif(nuc=='t' or nuc=='u'):
            nuc_t+=1
        elif(nuc=='g'):
            nuc_g+=1
        elif(nuc=='c'):
            nuc_c+=1
        #else:
        #    nuc_n+=1

    atprn=(float(nuc_a+nuc_t)/len(sequence))*100
    gcprn=(float(nuc_g+nuc_c)/len(sequence))*100

    print 'A:'+str(nuc_a)+',T:'+str(nuc_t)+',G:'+str(nuc_g)+',C:'+str(nuc_c)
    #print 'Total:%d'%(len(sequence)-nuc_n)

    if((atprn+gcprn)<80):
        print 'I am crazy about your intelligence !!!'
    else:
        print "A(T/U)%:"+str(atprn)
        print "GC%:"+str(gcprn)

def menu():
    print "=== MENU ==="
    print "1. Generate Sequence(DNA,RNA,Protein)"
    print "2. Generate PDF Sequence(DNA,RNA)"
    print "3. Check AT-GC% content"
    print "4. Get codons"
    print "5. Protein translation"
    print "6. Add sequence details"
    print "7. Exit"

def main():
    menu()
    check=True
    sequence=''
    while check:
        option=raw_input('Select option:')
        if(option=='1'):
            print "Sequence is being generated...."
            ln=raw_input('Enter sequence length:')
            tip=raw_input('Enter sequence type(dna,rna,protein):')
            if(ln!='' and ln!='0'):
                sequence=generateSequence(tip,int(ln))
                print 'Actual :'+sequence
                print 'Reverse:'+sequenceOperations(sequence,'revComp')
            else:
                continue

        elif (option=='2'):
            tip=raw_input('Enter sequence type(DNA,RNA):')
            if(tip!=''):
                sequence=generateSequencePDF(tip,284,(0.20,0.24,0.30,0.26))
                print 'Generated sequence:'+sequence
            else:
                print 'Please enter the sequence'

        elif (option=='3'):
            if(sequence!=''):
                atgcPercent(sequence)
            else:
                print 'Please enter the sequence'

        elif (option=='4'):
            if(sequence!=''):
                pos=input('Enter frame shift(+1,+2,+3 or -1,-2,-3):')
                if(pos==1 or pos==2 or pos==3 or pos==-1 or pos==-2 or pos==-3):
                    print "Sequence:"+sequence+" codons."
                    print getSeqCodons(sequence,pos)
                else:
                    print "Wrong frame shift position enter the right one"
            else:
                print 'Please enter the sequence'

        elif (option=='5'):
            #ln=raw_input('Enter sequence length:')
            pos=input('Enter frame shift(+1,+2,+3 or -1,-2,-3):')
            #sequence=generateSequence('dna',int(ln))
            #sequence="ATGAAAAAAATCGACGTTAAGATTCTGGACCCGCGCGTTGGGAAGGAATTTCCGCTCCCGACTTATGCCACCTCTGGCTCTGCCGGACTTGACCTGCGTGCCTGTCTCAACGACGCCGTAGAACTGGCTCCGGGTGACACTACGCTGGTTCCGACCGGGCTGGCGATTCATATTGCCGATCCTTCACTGGCGGCAATGATGCTGCCGCGCTCCGGATTGGGACATAAGCACGGTATCGTGCTTGGTAACCTGGTAGGATTGATCGATTCTGACTATCAGGGCCAGTTGATGATTTCCGTGTGGAACCGTGGTCAGGACAGCTTCACCATTCAACCTGGCGAACGCATCGCCCAGATGATTTTTGTTCCGGTAGTACAGGCTGAATTTAATCTGGTGGAAGATTTCGACGCCACCGACCGCGGTGAAGGCGGCTTTGGTCACTCTGGTCGTCAGTAA"
            protein=join(translateDNAtoProtein(sequence,pos),'')
            print 'Actual :'+sequence
            print 'Reverse:'+sequenceOperations(sequence,'revComp')
            print 'Protein sequence:'+protein


        elif (option=='6'):
            if(sequence!=''):
                print '\n\nGenerated protein:'+addDetails(sequence)
                print '\n\nActual DNA sequence:'+sequence
            else:
                print 'Please enter the sequence'

        else:
            print "Bye bye ..."
            break
main()
