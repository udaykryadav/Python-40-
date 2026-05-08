#to check wheater file matces contetn or not 
with open('8_this.txt', 'r') as f:
    content1 = f.read() 

with open('8_thisCopy.txt', 'r') as f:
    content2 = f.read()

if(content1 == content2):
    print('content is same ') 
else:
    print('contetn is not same ')