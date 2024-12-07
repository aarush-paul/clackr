import json
import time
import os
try:
    with open("n.json", "r") as f:
        names=json.load(f)
    with open("m.json", "r") as f:
        marks=json.load(f)
except:
    names=[]
    marks=[]
roll=[]

def encode():
    try:
        tnc=[]
        tmc=[]
        tpc=""
        h=""
        with open("n.json", "r") as f:
            tn=json.load(f)
        with open("m.json", "r") as f:
            tm=json.load(f)
        with open("p.json", "r") as f:
            tp=json.load(f)
        for i in tn:
            for j in i:
                h+=chr(ord(j)+26)
            tnc.append(h)
            h=""
        for i in tm:
            for j in i:
                h+=chr(ord(j)+26)
            tmc.append(h)
            h=""
        for i in tp:
            tpc+=chr(ord(i)+26)
        with open("n.json", "w") as f:
            json.dump(tnc,f)
        with open("m.json", "w") as f:
            json.dump(tmc,f)
        with open("p.json", "w") as f:
            json.dump(tpc,f)
    except:
        tpc=""
        with open("p.json", "r") as f:
            tp=json.load(f)
        for i in tp:
            tpc+=chr(ord(i)+26)
        with open("p.json", "w") as f:
            json.dump(tpc,f)

def decode():
    try:
        tnc=[]
        tmc=[]
        tpc=""
        h=""
        with open("n.json", "r") as f:
            tn=json.load(f)
        with open("m.json", "r") as f:
            tm=json.load(f)
        with open("p.json", "r") as f:
            tp=json.load(f)
        for i in tn:
            for j in i:
                h+=chr(ord(j)-26)
            tnc.append(h)
            h=""
        for i in tm:
            for j in i:
                h+=chr(ord(j)-26)
            tmc.append(h)
            h=""
        for i in tp:
            tpc+=chr(ord(i)-26)
        with open("n.json", "w") as f:
            json.dump(tnc,f)
        with open("m.json", "w") as f:
            json.dump(tmc,f)
        with open("p.json", "w") as f:
            json.dump(tpc,f)
    except:
        tpc=""
        with open("p.json", "r") as f:
            tp=json.load(f)
        for i in tp:
            tpc+=chr(ord(i)-26)
        with open("p.json", "w") as f:
            json.dump(tpc,f)
def table():
    decode()
    print()
    for i in range(1,len(names)+1):
        roll.append(str(i))
    print("+","-".center(10,"-"),"+","-".center(20,"-"),"+","-".center(20,"-"),"+")
    print("|","Roll".center(10),"|","Names".center(20),"|","Marks".center(20),"|")
    print("+","-".center(10,"-"),"+","-".center(20,"-"),"+","-".center(20,"-"),"+")
    for i in range(0,len(names)):
        print("|", roll[i].center(10), "|", names[i].center(20), "|", marks[i].center(20), "|")
    if names==[] and roll==[] and marks==[]:
        print("|", "<Records not available>".center(56), "|")
    print("+","-".center(10,"-"),"+","-".center(20,"-"),"+","-".center(20,"-"),"+")
    with open("n.json", "w") as f:
        json.dump(names, f)
    with open("m.json", "w") as f:
        json.dump(marks, f)
    encode()

def add():
    print()
    names.append(input("Name: "))
    marks.append(input("Marks: "))
    print()
    decode()
    with open("n.json", "w") as f:
        json.dump(names, f)
    with open("m.json", "w") as f:
        json.dump(marks, f)
    encode()
    print("[i] Record added successfully")
    print()
    time.sleep(1)
    

def delete(r):
    decode()
    names.pop(r-1)
    marks.pop(r-1)
    print()
    with open("n.json", "w") as f:
        json.dump(names, f)
    with open("m.json", "w") as f:
        json.dump(marks, f)
    print("[i] Record deleted successfully")
    print()
    time.sleep(2)
    encode()

def menu():
    while True:
        print()
        print("+", "-".center(30, "-"),"+")
        print("|","Welcome to Student TDBMS".center(30),"|")
        print("+","-".center(30, "-"),"+")
        print("(1) Display data")
        print("(2) Add record")
        print("(3) Delete record")
        print("(4) Logout")
        n=input("Enter Choice: ")
        if n=="1":
            table()
        elif n=="2":
            print()
            print("[i] Roll no. is auto assigned. Enter Students sequentially.")
            print()
            time.sleep(2)
            add()
        elif n=="3":
            table()
            print()
            print("[i] Deleting a record will result in roll no. reassignment")
            print()
            time.sleep(2)
            delete(int(input("Enter Roll no. of the data to be deleted: ")))
        elif n=="4":
            with open("n.json", "w") as f:
                json.dump(names, f)
            with open("m.json", "w") as f:
                json.dump(marks, f)
            print("[!] Logging out...")
            time.sleep(3)
            return False
        else:
            print()
            print("[!] Invalid Choice")
            print()
            time.sleep(2)
def login():
    while True:
        print()
        print("+", "-".center(30, "-"),"+")
        print("|","Login | Student TDBMS".center(30),"|")
        print("+","-".center(30, "-"),"+")
        print("(1) Enter Password")
        print("(2) Create Password(New login only)")
        print("(3) Reset")
        print("(4) Exit")
        o=input("Enter Choice: ")
        if o=="1":
            print()
            try:
                with open("p.json", "r") as f:
                    p=input("Enter Password: ")
                    decode()
                    if p==json.load(f) and p!="":
                        encode()
                        print()
                        print("[i] Login Successful")
                        print()
                        time.sleep(1)
                        print("[i] Never perform Keyboard Interrupt(Ctrl+C). This can result in data corruption.")
                        time.sleep(3)
                        print()
                        menu()
                    elif p=="":
                        print("[!] Wrong Password")
                        time.sleep(2)
                        encode()
                    else:
                        print("[!] Wrong Password")
                        time.sleep(2)
                        encode()
            except:
                print("[!] Password not set")
                print()
                time.sleep(2)
        elif o=="2":
            print()
            try:
                with open("p.json", "r") as f:
                    print("[!] Password already set")
                    print()
                    time.sleep(2)
            except:
                p=input("Set a password: ")
                with open("p.json", "w") as f:
                    json.dump(p,f)
                encode()
        elif o=="3":
            try:
                os.remove("m.json")
                os.remove("n.json")
                os.remove("p.json")
            except:
                print("[!] Data not found")
                print()
                time.sleep(2)
        elif o=="4":
            print()
            print("[!] Exiting...")
            time.sleep(3)
            return False
        else:
            print()
            print("[!] Invalid Choice")
            print()
            time.sleep(2)
login()