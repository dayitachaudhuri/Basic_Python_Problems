#WAP to print factorial of N taken from user

#ADDITIVE

N=int(input('Enter number : '))
prod=1
for i in range(1,N+1):
    prod*=i
print(prod)
    
#SUBTRACTIVE

num=int(input('Enter number : '))
d=num-1
while d>0 :
    num=num*d
    d=d-1
print(num)

#RECURSIVE

def fact(n):
    if n<0:
        return -1
    elif n<=1:
        return 1
    else:
        return n*fact(n-1)

num=int(input('Enter number : '))
print(fact(num))
    
