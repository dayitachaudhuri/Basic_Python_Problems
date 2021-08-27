fruits = ['red' ,'blue', 'pink', 'magenda',  'green','olive']

n=len(fruits)

for i in range(n):
    j=i-1
    key = fruits[i]
    while j >=0 and fruits[j] > key:
        fruits[j+1]=fruits[j]
        j -= 1
    else:
        fruits[j+1]=key

print(fruits)
