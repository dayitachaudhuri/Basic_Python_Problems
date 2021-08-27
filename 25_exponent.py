T=eval(input("Enter a tuple:"))
for i in range(0,len(T)):
    if (i+1)%3==0:
        print((int(T[i]))**3)
