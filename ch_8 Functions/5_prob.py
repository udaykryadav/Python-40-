'''
***
**
*

'''


def pattern(n):
    for i in range(n,0,-1):
        print('*'* i )

#recition way to solve this 
def patternR(n):
    if(n==0):
        return
    print('*' * n)
    patternR(n-1)



n = int(input('ener the value of n '))

patternR(n) 