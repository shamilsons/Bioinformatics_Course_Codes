from string import *
from random import *

#The Sequence class is a base class for other 2 classes (DNASeq, RNASeq)
class Sequence:
    #Constructor - runs when object of this class being instantiated
    def __init__(self):
        print "The Sequence class created"

    def showInfo(self):
        print "This is parent Sequence class"

    def getSeqLen(self):
        print "Returns the length of the particular sequence"

    #Destructor - runs when object of this class being deleted
    def __del__(self):
        print "Sequence class deleted"

class DNASeq(Sequence):
    nucSet=('A','T','G','C')

    def __init__(self,seqAccno,seqSet,seqOrg):
        self.seqAccno=seqAccno
        self.seqSet=seqSet
        self.seqLen=len(seqSet)
        self.seqOrg=seqOrg

    def generateSeq(self):
        counter=0
        seqDNA=[]

        if(self.seqLen<=0):
            self.seqLen=input("Enter DNA sequence length:")

        while counter<self.seqLen:
            idx=randint(0,3)
            seqDNA.append(DNASeq.nucSet[idx])
            counter=counter+1

        self.seqSet=join(seqDNA,"")

    def showInfo(self):
        print "This is a DNASeq class of:",self.seqOrg,"of",self.seqLen," bp(s)"
        print "DNA sequence\n"
        print self.seqSet

    def __del__(self):
        self.seqAccno=""
        self.seqLen=0
        self.seqOrg=""
        #print "This is a DNASeq before deletion class of: "+self.seqOrg+" of "+str(self.seqLen)+" bp(s)"


#Instatiating object of Sequence class
"""
seq1=Sequence()
seq1.showInfo()
seq1.getSeqLen()
del seq1
"""

seqDNA1=DNASeq("NT_X01417","", "E.coli")
seqDNA1.showInfo()
seqDNA1.generateSeq()
seqDNA1.showInfo()
#del seqDNA1
