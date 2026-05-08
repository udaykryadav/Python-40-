class calculator:
    def __init__(self,n):
        self.n=n

    def squre(self):
        print(f'the squraae of {self.n} is {self.n*self.n}')
    def cude(self):
        print(f'the squraae of {self.n} is {self.n*self.n*self.n}')
    def squreRoot(self):
        print(f'the squraae of {self.n} is {self.n**1/2}')

    @staticmethod
    def greet():
        print('hello there')


a =calculator(4)
a.greet()
a.squre()
a.cude()
a.squreRoot()