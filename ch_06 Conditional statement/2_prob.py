marks1=int(input('entre marks 1st '))
marks2=int(input('entre marks 2st '))
marks3=int(input('entre marks 3st '))


# check total percetage 

total_per= (100*(marks1+marks2+marks3))/300

if(total_per>=40 and marks3>=33 and marks2>= 33 and marks1>= 33):
    print("you are passed",total_per)

else:
    print("you failed , try next year ", total_per)