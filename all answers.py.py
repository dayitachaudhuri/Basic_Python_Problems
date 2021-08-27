#1
#WAP to print area of a circle with radius 3.75 m

import math
radius=3.75
area=math.pi*(radius**2)
print('Area of circle with radius 3.75 metres is',area,'square metres')

#2
#WAP to input 3 numbers from user and print their sum 

a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
c=int(input("Enter third number : "))

print("Sum of the three number is",a+b+c)

#3
#WAP to check is an integer is positive or negative

num=int(input('Enter the number : '))

if num==0:
  print(num,"is neither positive nor negative")
elif num>0:
  print(num,"is positive")
else:
  print(num,"is negative")

#4
#WAP to calculate simple interest

amount=int(input("Enter Amount Borrowed : Rs. "))
rate=float(input("Enter Rate of Interest (in percent) : "))
time=float(input("Enter Time(in years) : "))

si=amount*rate*time/100

a=amount+si

print("Simple Interest applicable is Rs.",si)
print("Total Amount to be Repayed is Rs.",a)

#5
# WAP to find the greatest out of 3 numbers

a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
c=int(input("Enter third number : "))

if a==b and b==c :
  print("The numbers are equal")
elif a>=b and a>=c :
  print("The largest number is",a)
elif b>=a and b>=c :
  print("The largest number is",b)
elif c>=a and c>=b :
  print("The largest number is",c)

#6
# WAP to check if an alphabet is vowel or not

char=input("Enter an alphabet : ")
vowel=['a','e','i','o','u','A','E','I','O','U']

if char in vowel :
  print(char,"is a vowel")
else :
  print(char,"is a consonant")

#7
#WAP to input marks in 3 subject, find their avegae and compute grades based on given criterion

a=int(input("Enter marks in first subject (out of 100) : "))
b=int(input("Enter marks in second subject (out of 100): "))
c=int(input("Enter marks in third subject (out of 100) : "))

avg=(a+b+c)/3

if avg>=80 :
  print("Grade - A")
  print("Level 4, above agency-normalised standards")

elif avg>=70 :
  print("Grade - B")
  print("Level 3, at agency-normalised standards")

elif avg>=60 :
  print("Grade - C")
  print("Level 2, below but approaching agency-normalised standards")

elif avg>=50 :
  print("Grade - D")
  print("Level 1, well-below agency-normalised standards")

elif avg>=40 :
  print("Grade - E")
  print("Level 1, too below agency-normalised standards")

else :
  print("Grade - R")
  print("Remedial standards")

#8
#WAP to print all numbers from 1 to 15

for i in range(1,16):
  print(i)


#9
# WAP to print sum of all numbers from 1 to 10

sum=0
for i in range(1,11):
  sum+=i
print(sum)

#10
#WAP to print all even numbers between 1 and 100

for i in range(1,101):
  if i%2==0:
    print(i)


#11
# WAP to print the pattern

# AAAAAAAA
# BBBBBBB
# CCCCCC
# EEEEE

alpha=['A','B','C','E']
n=8
for j in range(0,len(alpha)):
    for k in range(0,n):
      print(alpha[j],end='')
    print()
    n=n-1

#12

# WAP to print the pattern

# *
# **
# ***
# ****
# *****


for i in range(0,5):
    for j in range(0,i+1):
          print('*',end='')
    print()


#13   
'''
WAP to print the pattern

#
##
###
####
####
####
###
##
#

'''

for i in range(0,9):
        if i<4:
            for j in range(0,i+1):
                print('#',end='')
        elif i==4:
            for j in range(0,i):
                print('#',end='')
        elif i>4:
            for j in range(0,9-i):
                print('#',end='')
        print()


#14    
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


#15
#WAP to print factorial of N taken from user

N=int(input('Enter number : '))
prod=1
for i in range(1,N+1):
    prod*=i
print(prod)

    
#16
#WAP to print first 10 prime numbers

count=0
num=2
while count<10:
    for i in range(2,int(num-1)):
       if num%i==0:
          break
    else:
        print(num)
        count+=1
    num+=1

    
#17    
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

    
#18
#WAP to create a loop printing index of every i inn MISSISSIPPI

str="Mississippi"

for a in range(0,len(str)):
    if str[a]=='i':
        print(a)

#19
#WAP to print whether a given character is uppercase, lowercase, digit of any other special symbol

char=input("Enter a character :")

if char>='a' and char<='z' :
    print(char,"is a lowercase alphabet")
    
elif char>='A' and char<='Z' :
    print(char,"is an uppercase alphabet")
    
elif char>='0' and char<='9' :
    print(char,"is a digit")    

else:
    print(char,"is a special character")
    


    

   
