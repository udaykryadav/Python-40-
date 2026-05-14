try:
    a = int(input("Hey, Enter a number: "))
    print(a)

    
except Exception as e:
    print(e) 


#else used only if try was succesfull
else:
    print("I am inside else")