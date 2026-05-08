with open('6_log.txt','r') as f:
    content = f.read()

if('python' in content):
    print('python in content')
else:
    print("no pyhton in contetn")

