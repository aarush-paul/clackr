d={}
def menu():
    while True:
        print("MENU")
        print("(1) Enter Dictionary")
        print("(2) Add Record")
        print("(3) Delete Record")
        print("(4) Modify Phone Number")
        print("(5) Check Record")
        print("(6) Sort Dictionary")
        print("(7) Exit")
        o=input("Option: ")
        if o=="1": 
            takein()
        elif o=="2":
            add()
        elif o=="3":
            delete()
        elif o=="4":
            modify(input("Enter name to modify phone: "))
        elif o=="5": 
            check(input("Enter name to check: "))
        elif o=="6":
            sorter()
        elif o=="7":
            print("Exiting...")
            return False
        else:
            print("Invalid Option")

def sorter():
    global d
    d = dict(sorted(d.items()))
    print(d)

def check(c):
    if c in d:
        print(f"{c} exists in dictionary")
    else:
        print(f"{c} does not exist in dictionary")

def modify(m):
    print(d)
    d[m]=input("Enter new phone: ")
    print(d)

def delete():
    print(d)
    k=input("Enter name to delete: ")
    del d[k]
    print(d)

def add():
    print(d)
    nm=input("Name: ")
    pn=input("Phone number: ")
    d[nm]=pn
    print(d)

def takein():
    n=int(input("Enter number of friends: "))
    for i in range(n):
        nm=input("Name: ")
        pn=input("Phone number: ")
        d[nm]=pn
    print(d)

menu()