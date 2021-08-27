import matplotlib.pyplot as pl

l=[]
for i in range (1,6):
    n=int(input("Enter pass percentage : "))
    l.append(n)

pl.xlabel("Year")
pl.ylabel("Percentage")
year=['2015','2016','2017','2018','2019']
pl.bar(year,l)
pl.show()
