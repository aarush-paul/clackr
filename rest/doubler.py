n=input("Input terminal: ")
d=[]
for i in n:
    d.append(i)
for i in range(-1, -len(d), -1):
    print(2*d[i], end="")
print()