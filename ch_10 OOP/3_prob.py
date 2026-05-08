class demo:
    a = 4

o =  demo()
print(o.a) # print the class attribute because instace attribute is not present 

o.a=0 #inctance atttibute is set

print(o.a) #print the instacne  attrbute because instance attrbute is present 

print(demo.a)#print the class attribute  

#class attribute does not gets changed it just print the current intece attribute  