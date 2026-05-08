f = open("1poem.txt")
content = f.read()
if('twinkel' in content ):
    print('twinkel is present in file ')
else:
    print('twinkel is not in file ')


f.close