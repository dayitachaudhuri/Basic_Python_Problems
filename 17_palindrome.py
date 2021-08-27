#WAP to check if a given number is palindrome

a=int(input('Enter the number : '))
num=a
rev=0
while num>0 :
    digit=num%10
    rev=rev*10+digit
    num=num//10

if rev==a :
    print(a,'is a Palendrome')
else :
    print(a,'is not a Palendrome')

    
