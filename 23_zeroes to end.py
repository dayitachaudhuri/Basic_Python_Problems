num_list=eval(input("Enter a list:"))
a = [0 for i in range(num_list.count(0))]
x = [ i for i in num_list if i != 0]
x.extend(a)
print(x)
