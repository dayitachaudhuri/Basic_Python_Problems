amount=int(input("Enter Amount Borrowed : Rs. "))
rate=int(input("Enter Rate of Interest (per annum) : "))
time=int(input("Enter Time(in years) : "))

initial=amount

for i in range(0,time):
   amount=amount+(amount*rate/100)

ci=amount-initial

print('Compound interest is',ci)

