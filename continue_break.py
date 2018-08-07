#Import needed libraries
from random import *
from string import *

def main():
    control=True
    cnt_count=0
    brk_count=0
    rmn_count=0

    while control:
        rndNum=randint(0,100)

        if(rndNum>=90 and rndNum<100):
            brk_count+=1
            print 'Break executed, random number:%d'%(rndNum)
            break
        elif(rndNum>=5 and rndNum<15):
            cnt_count+=1
            print 'Continue executed, random number:%d'%(rndNum)
            continue
        else:
            rmn_count+=1
            print 'Remaing executed, randon number:%d'%(rndNum)


    total_count=float(brk_count+cnt_count+rmn_count)
    print '\nBreak execution probability:%1.2f'%(brk_count/total_count)
    print 'Continue execution probability:%1.2f'%(cnt_count/total_count)
    print 'Remaing execution probability:%1.2f'%(rmn_count/total_count)

#Calling a main function shows us from where magic begins
main()
