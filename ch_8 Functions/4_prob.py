def NS(n):
    if(n==1):
        return 1
    return NS(n-1)+n    


n = int(input('enter the value of n '))

print(f'{NS(n)}')
