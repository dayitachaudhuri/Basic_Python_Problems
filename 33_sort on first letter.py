fruits = ['guava' ,'grape', 'strawberry', 'apple',  'pomegranate','peach']
n=len(fruits)
for i in range(n):
        for j in range(0, n-i-1):
            if fruits[j][0] > fruits[j+1][0] :
                fruits[j], fruits[j+1] = fruits[j+1], fruits[j]
print(fruits)
