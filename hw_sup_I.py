from string import *
from random import *
"""
def addError(status):
    num=randint(1,10)
    #print "Number:",num
    if(num<=5):
        return not(status)
    else:
        return status
def getPatientStatus(lm,hp):
    #The algorithm checks all the paramets and
    #returns 0/1
    #lm:350-800 and hp:0/1
    status=''
    if((lm>=350 and lm<=800) and hp==0):
        status=False
    else:
        status=True
    return status
def main():
    print "lm:350-800 and hp:0"
    for i in range(1,11):
        lm=randint(100,1200)
        hp=randint(0,1)
        print str(i)+".lm:"+str(lm)+" hp:"+str(hp)+" actual:"+str(getPatientStatus(lm,hp))+" predicted:"+str(addError(getPatientStatus(lm,hp)))
main()
"""

seqFile=open('test.txt',"w")
print "File has been created ..."
counter=0
while counter<10:
    seqFile.write(str(10+counter)+'\t'+str(30+counter)+'\t'+str(60+counter)+'\n')
    counter+=1
seqFile.close()
print 'file closed'

data={}
seqFile=open('test.txt',"r")
print 'File opened for reading'
sequences=seqFile.readlines()
count=1
for sequence in sequences:
    #if(count==1):
        #print type(sequence)
    data[count]=split(sequence.strip(),'\t')
    count+=1
seqFile.close()
print data[1]
