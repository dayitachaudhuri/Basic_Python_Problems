dic={"jenny":"abc123","jack":"cde456","joseph":"fgh789","angel":"ijk123","mary":"lmn456","george":"opq789","leo":"rst123"}
username=list(dic.keys())

a=input("Enter Username:")
b=input("Enter password:")

if a in username:
    if b==dic[a]:
        print("You are successfully logged in")
    else:
        print("Invalid password")
else:
    print("Invalid User")    
