filename=input("enter name of file: ")
a=open(filename,"r")
dat=a.read()
count=0
for i in dat:
        if i in ['u','o','i','e','a']:
            count+=1
a.close()
print(count)
