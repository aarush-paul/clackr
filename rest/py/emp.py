n=int(input("Enter number of employees: "))
d={}
for i in range(n):
    n=input("Enter name: ")
    a=int(input("Enter age: "))
    s=int(input("Enter salary: "))
    d[n]=[a,s]
print("Old Dictionary: ", d)
for i in d:
    j=d[i]
    if j[0]>=55:
        j[1]+=j[1]/5
print("New Dictionary: ", d)