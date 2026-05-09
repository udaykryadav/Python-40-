class emp:
    salary= 234
    incement = 20

    @property
    def salaryAfter(self):
        return (self.salary+ self.salary*(self.incement/100))
    
    @salaryAfter.setter
    def salaryAfter(self, salary):
        self.incement= ((salary/self.salary)-1)*100
    


e = emp()
print(e.salaryAfter)
e.salaryAfter = 280
print(e.incement)
