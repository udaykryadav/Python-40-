class employer:
    company='ITC'
    name = 'default name'
    def show(self):
        print(f'the name of the employe is {self.name} and salary is {self.company}')
    
class coder:
    lan='py'

    def printLan(self):
        print(f'good at this lan {self.lan}')

class programmer(employer,coder):

    company ='ITC infotech'
    def showlan(self):
        print(f'the name is {self.company} and he is good with {self.lan} language')


a= employer()
b=programmer()

b.show()
b.printLan()
b.showlan()
