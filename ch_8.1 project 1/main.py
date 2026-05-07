import random
'''
-1
0
1
'''

computer = random.choice([-1,0,1])
youstr = input('enter your choice ')
youdict={'s':1,'w':-1 ,'g':0}
reverdict={1:'snake',-1:'water',0:'gun'}

you =youdict[youstr]

print(f'you chose {reverdict[you]}\n computer chose {reverdict[computer]}')

# if(computer==you):
#     print('its a draw')

# else:
#     if(computer==-1 and you==1):
#         print('you win')
#     elif(computer==-1 and you==0):
#         print('you lose')
#     elif(computer==1 and you==-1):
#         print('you lose')
#     elif(computer==1 and you==0):
#         print('you win')
#     elif(computer==0 and you==-1):
#         print('you win')
#     elif(computer==0 and you==1):
#         print('you win')
#     else:
#         print('somehting went wrong')

if((computer - you ) == -1 or (computer-you) ==2 ):
    print('you loose')
else:
    print('you winn')