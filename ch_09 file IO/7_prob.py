with open('6_log.txt','r') as f:
    lines = f.readlines()

lineno=1
for line in lines:
    if('python' in line):
        print(f'python in content line number {lineno}')
        break
    lineno +=1

else:
    print("no pyhton in content ")
