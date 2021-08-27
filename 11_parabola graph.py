import matplotlib.pyplot as plt

a=[]
b=[]

for x in range(-50,50):
    y=x**2
    a.append(x)
    b.append(y)

plt.plot(a,b)

plt.show()
