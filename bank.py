import time
import json
empu=[]
empp=[]
cusu=[]
cusp=[]
masteru="Nqzv{v\u0080\u0081\u007fn\u0081|\u007f"
masterp="Nqzv{MefgOn{x"
def encode(t):
    ft=""
    for i in str(t):
        ft+=chr(ord(i)+len(t))
    return ft

def decode(t):
    ft=""
    for i in str(t):
        ft+=chr(ord(i)-len(t))
    return ft


def main():
    while True:
        masteru="Nqzv{v\u0080\u0081\u007fn\u0081|\u007f"
        masterp="Nqzv{MefgOn{x"
        print("+", "-".center(30,"-"),"+")
        print("|","Welcome to XYZ Bank".center(30),"|")
        print("+", "-".center(30,"-"),"+")
        print("(1) Customer Login")
        print("(2) Employee Login")
        print("(3) Exit")
        print()
        c=input("Enter Choice(1-3): ")
        if c=="1":
            customerlogin()
        elif c=="2":
            employeelogin()
        elif c=="3":
            print()
            print("[i] Exiting")
            time.sleep(5)
            return False
        elif c==decode(masteru):
            print("[i] Admin Login detected")
            print()
            n=input("Enter Admin Password: ")
            if n==decode(masterp):
                print("[i] Login Successful")
                time.sleep(1)
                print("[i] Encrypting data...")
                time.sleep(3)
                print("[i] Checking for Vulnerabilities...")
                time.sleep(2)
                print("[i] Redirecting...")
                time.sleep(1)
                print()
                admindash()
        else: 
            print()
            print("[!] Invalid Option")
            print()
            time.sleep(2)

def admindash():
    while True:
        print("+", "-".center(30,"-"),"+")
        print("|","XYZ Bank | Admin Dashboard".center(30),"|")
        print("+", "-".center(30,"-"),"+")
        print("(1) Display Employee List")
        print("(2) Display Customer List")
        print("(3) Enroll Employee")
        print("(4) Exit")
        n=input("Enter Choice(1-4): ")
        if n=="1": 
            dispemp()
        elif n=="2":
            dispcus()
        elif n=="3": 
            enroll()
        elif n=="4":
            print()
            print("[i] Logging out...")
            time.sleep(5)
            return False
        else: 
            print()
            print("[!] Invalid Option")
            print()
            time.sleep(2)
def enroll():
    print()
    m=input("Enter username: ")
    n=input("Enter password: ")
    try:
        with open("empu.json", "r") as f:
            empu=decode(json.load(f))
        with open("empp.json", "r") as f:
            empp=decode(json.load(f))
    except:
        empu.append(m)
        empp.append(n)
        with open("empu.json", "w") as f:
            json.dump(encode(empu), f)
        with open("Empp.json", "w") as f:
            json.dump(encode(empp), f)
        empu.append(m)
        empp.append(n)
        with open("empu.json", "w") as f:
            json.dump(encode(empu), f)
        with open("Empp.json", "w") as f:
            json.dump(encode(empp), f)


def dispemp():
    print()
    print("+", "-".center(20,"-"),"+", "-".center(20,"-"), "+")
    print("|","Username".center(20),"|", "Password".center(20), "|")
    print("+", "-".center(20,"-"),"+", "-".center(20,"-"), "+")
    try:
        with open("empu.json", "r") as f:
            empu=decode(json.load(f))
        with open("empp.json", "r") as f:
            empp=decode(json.load(f))
    except:
        print("", end="")
    if empu==[] and empp==[]:
        print("|", "<no records available>".center(40),"|")
    else:
        for i in range(0, len(empu)):
            print("|",empu[i].center(20),"|", empp[i].center(20), "|")
    print("+", "-".center(20,"-"),"+", "-".center(20,"-"), "+")

def dispcus():
    print()
    print("+", "-".center(20,"-"),"+", "-".center(20,"-"), "+")
    print("|","Username".center(20),"|", "Password".center(20), "|")
    print("+", "-".center(20,"-"),"+", "-".center(20,"-"), "+")
    try:
        with open("cusu.json", "r") as f:
            cusu=decode(json.load(f))
        with open("cusp.json", "r") as f:
            cusp=decode(json.load(f))
    except:
        print("", end="")
    if cusu==[] and cusp==[]:
        print("|", "<no records available>".center(40),"|")
    else:
        for i in range(0, len(cusu)):
            print("|",cusu[i].center(20),"|", cusp[i].center(20), "|")
    print("+", "-".center(20,"-"),"+", "-".center(20,"-"), "+")

def employeelogin():
    ename=[]
    epass=[]
    while True:
        print("+", "-".center(30,"-"),"+")
        print("|","XYZ Bank | Employee Login".center(30),"|")
        print("+", "-".center(30,"-"),"+")
        print()
        try:
            with open("ename.json", "r") as f:
                ename=decode(json.load(f))
            with open("epass.json", "r") as f:
                epass=decode(json.load(f))
            if ename==[] and epass==[]:
                print("[!] Account database empty. Contact Bank. ")
                print()
                time.sleep(2)
                return False
        except:
            print("[!] Account database empty. Contact Bank. ")
            print()
            time.sleep(2)
            return False
        n=input("Enter username: ")
        p=input("Enter password: ")
        if n in ename:
            i=ename.index(n)
            if epass[ename.index(n)]==p:
                print()
                print(f"[i] Login Successful. Welcome {n}")
                print()
                time.sleep(2)
                empdash(n)
        elif n==decode(masteru) and p==decode(masterp):
            print()
            print("[i] Admin Login detected")
            time.sleep(1)
            print("[i] Encrypting data")
            time.sleep(2)
            print("[i] Checking for Vulnerabilities")
            time.sleep(2)
            print("[i] Login Successful")
            time.sleep(1)
            print()
            admindash()    

def empdash(p):
    while True:
        print("+", "-".center(30,"-"),"+")
        print("|","XYZ Bank | Employee Dashboard".center(30),"|")
        print("+", "-".center(30,"-"),"+")
        print()
        print(f"Name: {p}")
        print()
        print("(1) Create Account")
        print("(2) Close Account")

def customerlogin():
    cname=[]
    cpass=[]
    while True:
        print("+", "-".center(30,"-"),"+")
        print("|","XYZ Bank | Customer Login".center(30),"|")
        print("+", "-".center(30,"-"),"+")
        print()
        try:
            with open("cname.json", "r") as f:
                cname=json.load(f)
            with open("cpass.json", "r") as f:
                cpass=json.load(f)
            if cname==[] and cpass==[]:
                print("[!] Account database empty. Contact Bank. ")
                print()
                time.sleep(2)
                return False
        except:
            print("[!] Account database empty. Contact Bank. ")
            print()
            time.sleep(2)
            return False
        n=input("Enter username: ")
        p=input("Enter password: ")
        if n in cname:
            i=cname.index(n)
            if cpass[cname.index(n)]==p:
                print()
                print(f"[i] Login Successful. Welcome {n}")
                print()
                time.sleep(2)
                cusdash(n)
        
def cusdash(o):
    while True:
        print("+", "-".center(30,"-"),"+")
        print("|","XYZ Bank | Customer Dashboard".center(30),"|")
        print("+", "-".center(30,"-"),"+")
        print()
        print(f"Name: {o}")

main()