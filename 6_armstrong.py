a=int(input('Enter the number : '))
num=a
rem=0
while num>0 :
    rem+=(num%10)**3
    num=num//10

if rem==a :
    print(a,'is an Armstrong Number')
else :
    print(a,'is  not an Armstrong Number')

    
