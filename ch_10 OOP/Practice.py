# OOP is a programing approce which make sure you DRY do't repeat yourself
#useing reuseable code

class emp:
    lan='eng'
    salaary='300000000000000' #class attribute
    
    # we have to pass any argument we use it or not
    def getInfo(self):
        print(f'the lan is {self.lan} ,  the salaray is {self.salaary}')

    def greet(self):
        print(f'good morning {self.name}') 
    
    @staticmethod #when we do not want any property of object 
    def greet():
        print(f'good morning')

uday = emp()
uday.name='uday' # object instance attribute 
#uday.lan='py'  #intance attribut >>>>>>> class attribute
#print(uday.name,uday.lan)

uday.getInfo()
# emp.getInfo(uday) #same as above line 
uday.greet() 


