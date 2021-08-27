#WAP to calculate simple interest


amount=int(input("Enter Amount Borrowed : Rs. "))
rate=float(input("Enter Rate of Interest (in percent) : "))
time=float(input("Enter Time(in years) : "))

si=amount*rate*time/100

a=amount+si

print("Simple Interest applicable is Rs.",si)
print("Total Amount to be Repayed is Rs.",a)
