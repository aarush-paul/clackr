d1={'a':1,'b':2,'c':3}
d2={}
a=0
for i in d1:
    a+=d1[i]
for i in d1:
    d2[i]=a
print(d2)