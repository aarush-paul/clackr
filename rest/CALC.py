import json
def encode(t):
    ft=""
    for i in str(t):
        ft+=chr(ord(i)+len(t))
    return ft
n=input("Str: ")
with open("test.json", "w") as f:
    json.dump(encode(n), f)
print("Encoded: ", encode(n))