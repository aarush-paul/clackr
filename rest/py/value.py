d1=eval(input("Enter dictionary 1: "))
d2=eval(input("Enter dictionary 2: "))
d1v=[]
d2v=[]
print("Values with different keys: ", end="")
for i in d1:
    d1v.append(d1[i])
for i in d2:
    d2v.append(d2[i])
for i in d1v:
    if i in d2v:
        if d1v.index(i)!=d2v.index(i):
            print(i, end="")
