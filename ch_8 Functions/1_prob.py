def gretes(n1,n2,n3):
    if(n1>n2 and n1>n3):
        return n1
    elif(n2>n1 and n2>n3):
        return n2
    elif(n3>n1 and n3>n2):
        return n3
    

n1= int(input('enter first number '))
n2= int(input('enter second number '))
n3= int(input('enter third number '))

print(f'greatest number is {gretes(n1,n2,n3)}')