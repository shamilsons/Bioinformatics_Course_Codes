from string import *

#Declare subjects
gbe403={101:[70,80,40,60], 102:[20,30]}
gbe308={101:[50,10,70,20]}
gbe399={101:'S'}

#Declare students
std1=('Ahmet', 'Yilmaz', "Male", (gbe403[101], gbe308[101],gbe399[101]))
std2=('Ayse', 'Yildiz', 'Female', (gbe403[102]))

#Declare class4
class4={101:std1, 102:std2}

#Get all student grades in subject GBE403
std1_sbjs=class4[101][3][0]
print std1_sbjs
print "Std 1 average:\n"+str(0.1*std1_sbjs[0]+0.1*std1_sbjs[1]+0.3*std1_sbjs[2]+0.5*std1_sbjs[3])
