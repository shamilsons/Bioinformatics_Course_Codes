from string import *

grade=int(raw_input('Enter grade:'))

#1.if-elif-else and logical operators
'''
if(grade>=90 and grade<=100):
    print 'Student got AA'
elif (grade>=80 and grade<=89):
    print 'Student got BA'
elif (grade>=75 and grade<=79):
    print 'Student got BB'
elif (grade>=70 and grade<=74):
    print 'Student got BC'
elif (grade>=65 and grade<=69):
    print 'Student got CC'
elif (grade>=60 and grade<=64):
    print 'Student got CD'
elif (grade>=50 and grade<=59):
    print 'Student got DD'
else:
    print 'Student got FF'
'''

#2.if-else and logical operators
'''
if(grade>=90 and grade<=100):
    print 'Student got AA'
else:
    if (grade>=80 and grade<=89):
        print 'Student got BA'
    else:
        if (grade>=75 and grade<=79):
            print 'Student got BB'
        else:
            if (grade>=70 and grade<=74):
                print 'Student got BC'
            else:
                if (grade>=65 and grade<=69):
                    print 'Student got CC'
                else:
                    if (grade>=60 and grade<=64):
                        print 'Student got CD'
                    else:
                        if (grade>=50 and grade<=59):
                            print 'Student got DD'
                        else:
                             print 'Student got FF'
'''

#3.if-else only
if(grade<=100):
    if(grade>=90):
        print 'Student got AA'
    else:
        if(grade<=89):
            if(grade>=80):
                print 'Student got BA'
            else:
                if(grade<=79):
                    if(grade>=75):
                        print 'Student got BB'
                    else:
                        if(grade<=74):
                            if(grade>=70):
                                print 'Student got BC'
                            else:
                                if(grade<=69):
                                    if(grade>=65):
                                        print 'Student got CC'
                                    else:
                                        if(grade<=64):
                                            if(grade>=60):
                                                print 'Student got CD'
                                            else:
                                                 if(grade<=59):
                                                    if(grade>=50):
                                                        print 'Student got DD'
                                                    else:
                                                        print 'Student got FF'
