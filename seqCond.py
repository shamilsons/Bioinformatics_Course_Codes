from string import *
from random import *

def main():
    seqBio1="ATTTGGCCCNNTTAAATGTTTTNAAAAGGNCCATGCN"
    seqBio2="ACGAUGUCCGGCCCNNAGUGNGCAAUAAGCC"
    seqSet=[seqBio1,seqBio2]
    rdnnum=randint(0,1)
    print "Random number:",rdnnum
    if 'U' in seqSet[rdnnum]:
        print "This is an RNA sequence"
        print "Number of Ns in SeqBio1",count(seqBio1,'N')
        print "Number of Ns in SeqBio2",count(seqBio2,'N')

        if count(seqBio1,'N')==count(seqBio2,'N'):
            print "Number of Ns are equal"
        elif count(seqBio1,'N')>count(seqBio2,'N'):
            print "SeqBio1 has more Ns"
        else:
            print "SeqBio2 has more Ns"
    else:
        print "This is DNA sequence"
        print "Seq1 len:",len(seqBio1)
        print "Seq2 len:",len(seqBio2)
        if len(seqBio1)==len(seqBio2):
            print "Seq 1 and Seq2 are equal in length"
        elif len(seqBio1)<len(seqBio2):
            print "Seq 1 is smaller than Seq2 in length"
        else:
            print "Seq 1 is bigger than Seq2 in length"
  
  main()
