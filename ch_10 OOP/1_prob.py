class programmer:
    company='microsoft'

    def __init__(self,name,salary, pin):
        self.name=name
        self.salary=salary
        self.pin=pin
        
u = programmer('uday', 13000000000 ,1000000)
print(u.name,u.company,u.pin,u.salary)
r = programmer('rday', 13000000000 ,1000000)
print(r.name,r.company,r.pin,r.salary)
