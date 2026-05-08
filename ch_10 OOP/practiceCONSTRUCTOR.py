# OOP is a programing approce which make sure you DRY do't repeat yourself
#useing reuseable code

class emp:
    lan='eng'
    salary='300000000000000'

    def __init__(self,name,salary,lan):  # dunder methood gets automaticely called 
        self.name=name
        self.salary=salary
        self.lan=lan
        print("i am creating and object ")      
    
uday = emp('HARRY',1300000,'JAVA')

print(uday.name,uday.lan)
