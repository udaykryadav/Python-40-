p1 = "make a lot of money"
p2 = "Buy now"
p3 = "sub"
p4 = "click this "


message = input("enter your message ")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("spam message")

else:
    print("not a spam ")