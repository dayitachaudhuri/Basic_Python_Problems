import matplotlib.pyplot as plt

plt.axis("equal")
contri=[19,8,12,17,19,20]
name=["Toilet","Other","Leak","Household Chores","Drinking","Shower"]
expl=[0.05,0.05,0.05,0.05,0.05,0.05]
plt.pie(contri,labels=name,autopct="%1.1f%%", explode=expl)
plt.show()
