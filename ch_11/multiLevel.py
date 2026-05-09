class employee:
    a=0
class programmer(employee):
    b=1
class manager(programmer):
    c=2


e=employee()
print(e.a)

p=programmer()
print(p.b , p.a)

m=manager()

print(m.c, m.b, m.a)