from string import *
from random import *

def main():
    #Student id's 101, 102
    data_std1=[['AHMET', 'SARIGUL'],[[['GBE-403'],[80,95,40,10]],[['GBE-515'],[20,40,60,90]]]]
    data_std2=[['MINE', 'KAYA'],[[['GBE-403'],[10,40,95,80]],[['GBE-515'],[90,60,25,40]]]]
    #Our class
    cls1={101:data_std1,102:data_std2}
    print 'CLASS COURSE GRADES'
    print '-----------------------------'
    print 'Student 1:'+cls1[101][0][0]+' '+cls1[101][0][1]
    print 'Course:'+cls1[101][1][0][0][0]+':'+str(0.05*cls1[101][1][0][1][0]+0.05*cls1[101][1][0][1][1]+0.3*cls1[101][1][0][1][2]+0.6*cls1[101][1][0][1][3])
    print 'Course:'+cls1[101][1][1][0][0]+':'+str(0.05*cls1[101][1][1][1][0]+0.05*cls1[101][1][1][1][1]+0.3*cls1[101][1][1][1][2]+0.6*cls1[101][1][1][1][3])
    print '-----------------------------'
    print 'Student 1:'+cls1[102][0][0]+' '+cls1[102][0][1]
    print 'Course:'+cls1[102][1][0][0][0]+':'+str(0.05*cls1[102][1][0][1][0]+0.05*cls1[102][1][0][1][1]+0.3*cls1[102][1][0][1][2]+0.6*cls1[102][1][0][1][3])
    print 'Course:'+cls1[102][1][1][0][0]+':'+str(0.05*cls1[102][1][1][1][0]+0.05*cls1[102][1][1][1][1]+0.3*cls1[102][1][1][1][2]+0.6*cls1[102][1][1][1][3])
    #print float(sum(cls1[101][1][1])/len(cls1[101][1][1]))
    #print float(sum(data_std1[2])/len(data_std1[2]))

main()
