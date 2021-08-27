#WAP to take N from the user and print fibonacci series upto N terms

N=int(input("Enter the number of terms of sequence : "))

n1,n2=0,1

if N>=1:
    print(n1)
    if N>=2:
        print(n2)
        if N>2:
            for i in range(0,N-2):
                n=n1+n2
                print(n)
                n1,n2=n2,n
else:
    print("Please enter a valid positive integer")
