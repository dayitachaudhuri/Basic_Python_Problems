a={'janet':{"eng":23,"math":45,"science":30},'jack':{"eng":40,"math":39,"science":35}}
b=a.keys()
for i in b:
    print(i)
    for j in a[i]:
        print(j,":",a[i][j])
    print()
