filesource=input("enter name of source file: ")
filetarget=input("enter name of target file: ")
a=open(filesource,"r")
b=open(filetarget,"w")
dat=a.readlines()
lines=""
for i in dat:
    if "p" in i:
        lines=lines+i
b.write(lines)
a.close()
b.close()

