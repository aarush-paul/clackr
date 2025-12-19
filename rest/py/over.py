d1=eval(input("Enter D1: "))
d2=eval(input("Enter D2: "))
for i in d1:
    if i in d2:
        print(i, end=",")
print("are the overlapping keys.")