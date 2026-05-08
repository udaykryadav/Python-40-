word ='donkey'

with open('4_file.txt','r') as f:
    content = f.read()

newContent= content.replace(word,"######")

with open('4_file.txt', 'w' ) as f:
    f.write(newContent)