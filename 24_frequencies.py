my_list=eval(input("Enter a list :"))
freq = {} 
for item in my_list: 
        if (item in freq): 
            freq[item] += 1
        else: 
            freq[item] = 1
  
for key, value in freq.items(): 
        print ("% d : % d"%(key, value)) 
