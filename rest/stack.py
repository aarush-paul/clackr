d=[]
def menu():
    while True:
        print("(1) Push")
        print("(2) Pop")
        print("(3) Display")
        print("(4) Exit")
        o=input("Enter option: ")
        if o=="1":
            push()
        elif o=="2":
            pop()
        elif o=="3":
            print(d)
        else:
            return False

def push():
    n=input("Enter name: ")
    p=int(input("Enter pincode: "))
    d.append([n,p])

def pop():
    d.pop(-1)

menu()