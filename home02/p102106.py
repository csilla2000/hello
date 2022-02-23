a=int(input("Adjon meg egy számot!"))
b=0
c=0
while a!=0:
    b=b+a
    c=c+1
    a = int(input("Adjon meg egy számot!"))

print("{:.2f}".format(b/c))

