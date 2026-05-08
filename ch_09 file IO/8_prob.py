with open('8_this.txt','r') as f:
    content = f.read()

with open('8_thisCopy.txt','w') as f:
    f.write(content)