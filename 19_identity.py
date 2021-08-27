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
    


    

