from string import *
from random import *

dnaNucs=('A','T','G','C')

def genDNASeq(seqLen):
    counter=0
    seqDNA=[]

    while counter<seqLen:
        idx=randint(0,3)
        seqDNA.append(dnaNucs[idx])
        counter=counter+1

    return seqDNA

def recordSequence(seqBio, opt):
    if(opt=='write'):
        seqfile = open("sequences.txt", "wb+")
        seqfile.write(seqBio);
        seqfile.close()
        print "Record process over successfully"
    else:
        numNucs=raw_input("How many nucs you wanna read (for specific position enter with -):")
        seqfile = open("sequences.txt", "r+")
        pos=split(numNucs,"-")
        if(len(pos)>1):
            sequence = seqfile.read()
            return sequence[int(pos[0]):int(pos[1])]
        elif(len(pos)==1):
            sequence = seqfile.read(int(pos[0]))
            return sequence
        else:
            sequence = seqfile.read()
            return sequence

def genSeqPDF(seqType, seqSize, pdf):

    seqProduct=[]
    #creating a pool of nucleotides

    if(sum(pdf)==1):
        nuc_A=(seqSize*pdf[0])*100
        nuc_T=(seqSize*pdf[1])*100
        nuc_G=(seqSize*pdf[2])*100
        nuc_C=(seqSize*pdf[3])*100

        if(seqType=="dna"):
            while(seqSize>0):
                #lets select nucleotides with 0.25 probability
                slcvar=randint(0,4)
                if(slcvar==0 and nuc_A>0):
                    nuc_A=nuc_A-1
                    seqProduct.append("A")
                elif(slcvar==1 and nuc_T>0):
                    nuc_T=nuc_T-1
                    seqProduct.append("T")
                elif(slcvar==2 and nuc_G>0):
                    nuc_G=nuc_G-1
                    seqProduct.append("G")
                else:
                    if(nuc_C>0):
                        nuc_C=nuc_C-1
                        seqProduct.append("C")

                seqSize=seqSize-1

        return join(seqProduct,'')
    else:
        print "WARNING MESSAGE: Your PDF of nucleotides doesnot equal to 1, re-enter"

def nucStatistics(seqBio):
    nucA=count(seqBio,'A')
    nucT=count(seqBio,'T')
    nucG=count(seqBio,'G')
    nucC=count(seqBio,'C')
    """
    for nt in seqBio:
        if nt=='A':
            nucA+=1
        elif nt=='T':
            nucT+=1
        elif nt=='G':
            nucG+=1
        else:
            nucC+=1
    """
    print "A nucleotide statistics:",float(nucA)*100/len(seqBio)
    print "T nucleotide statistics:",float(nucT)*100/len(seqBio)
    print "G nucleotide statistics:",float(nucG)*100/len(seqBio)
    print "C nucleotide statistics:",float(nucC)*100/len(seqBio)

mySeq=genSeqPDF("dna", 10000, [0.35, 0.15, 0.10, 0.40])
print "The generated sequence:"+mySeq
print nucStatistics(mySeq)

def startstopSignals(seqBio):
    startCodons=count(seqBio,'ATG')
    stopCodons=count(seqBio,'TAA')
    print "ATG number:",startCodons
    print "TAA number:",stopCodons

def prgMenu():
    print "== MENU =="
    print "1. Generate DNA sequence"
    print "2. Nucleotide statistics"
    print "3. Search start-stop signals"
    print "4. Store sequence"
    print "5. EXIT"

def main():
    checkMenu=True

    prgMenu()
    seqBio=""
    while checkMenu:
        option=raw_input("\nEnter option:")
        if(option=='1'):
            seqLen=input("Enter sequence length:")
            if seqLen>0:
                seqBio=join(genDNASeq(seqLen),'')
                print seqBio
            else:
                print "\nERROR MESSAGE: Enter proper sequence length\n"

        elif option=='2':
            if len(seqBio)>0:
                nucStatistics(seqBio)
            else:
                print "\nERROR MESSAGE: First create a biological sequence\n"

        elif option=='3':
            if len(seqBio)>0:
                startstopSignals(seqBio)
            else:
                print "\nERROR MESSAGE: First create a biological sequence\n"

        elif option=='4':
            if len(seqBio)>0:
                if(raw_input("Enter option (read/write):")=="write"):
                    recordSequence(seqBio,"write")
                else:
                    print recordSequence(seqBio,"read")
            else:
                print "\nERROR MESSAGE: First create a biological sequence\n"
        else:
            break


#main()
