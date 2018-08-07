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
        check=randint(1,4)
        if(check==1 and num_a!=0):
            product.append('A')
            num_a=num_a-1
        elif(check==2 and num_t!=0):
            product.append('T')
            num_t=num_t-1
        elif(check==3 and num_g!=0):
            product.append('G')
            num_g=num_g-1
        elif(check==4 and num_c!=0):
            product.append('C')
            num_c=num_c-1
        else:
            continue

        counter+=1

    print "Nucleotide sets after generating sequence"
    print "A nuc set:%d"%(num_a)
    print "T nuc set:%d"%(num_t)
    print "G nuc set:%d"%(num_g)
    print "C nuc set:%d"%(num_c)

    return product

def main():
    seqDNA=genSequenceDP(10,0,(0.15, 0.15, 0.35, 0.35))
    print join(seqDNA, '')
    print len(seqDNA)

main()
