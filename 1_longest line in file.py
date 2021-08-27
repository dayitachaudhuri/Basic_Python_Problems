def stats(filename):
    longest=""
    lines=open(filename,"r").readlines()
    for i in lines:
        if len(i)>len(longest):
               longest=i
        
    return longest

a=input("enter name of file: ")
print(stats(a))
