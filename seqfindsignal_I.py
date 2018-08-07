from string import *

#Variables used for finding start codons
start_codon_index=-1
stop_codon_index=-1
#Variables used for finding stop codons
start_codon_count=0
stop_codon_count=0

seqDNA='AGGTATGGGCCTTTAAAGTG'

start_codon_index=find(seqDNA,'ATG')
start_codon_count=count(seqDNA,'ATG')
stop_codon_index=find(seqDNA,'TAA')
stop_codon_count=count(seqDNA,'TAA')

#Statistics of start and stop codons
print "============= STATISTICS =========="
print "ATG Index:"+str(start_codon_index)
print "ATG count:"+str(start_codon_count)
print "TAA Index:"+str(stop_codon_index)
print "TAA count:"+str(stop_codon_count)
print "----------------------------------"
