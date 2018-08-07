class Person:
    name=''
    surname=''
    gender=''
    age=''

    def __init__(self,name,surname,gender):
        self.name=name
        self.surname=surname
        self.gender

    def displayInfo(self):
        print 'This is a class Person'
        print 'Name:'+self.name+' '+self.surname+' Gender:'+self.gender

    def setAge(self,age):
        self.age=age

    def getAge(self):
        return self.age

def main():
    bus=[]
    prs1=Person('John', 'Watson','Male')
    prs1.displayInfo()
    prs1.setAge(18)
    print prs1.getAge()
    prs1.age=24
    print prs1.age

    prs2=Person('Cem', 'Yilmaz','Male')
    prs2.displayInfo()

    if(prs1==prs2):
        print 'Objects are same'
    else:
        print 'Objects are different'

    bus.append(prs1.name)
    bus.append(prs2.name)

    print bus

main()
