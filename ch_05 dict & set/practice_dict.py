#look up / searching is fast in dictionary 
A=  {} #empty dictionary

marks = {
    'harry': 13,
    'uday': 15,
    'don': 16,
    0:"rohan"
}

print(marks, type(marks))

# dictionary are 
# UNORDERD 
# MUTABLE
# CANT'N CONTAIN DUPLICATE KEY 

print(marks.items()) #gives list of key value pairs which are in the form of tuple # [(),(),()]
print(marks.keys()) 


marks.update({'harry' : 99})
marks.update({'renuka' : 99}) #if key is not in the dicttinory it gets added and if its present it gets updated 


print(marks, type(marks))

print(marks.get("harry")) #this will give none as output if key does not exist
print(marks["harry"]) #this will give the key error if it does not exist in dictinory
