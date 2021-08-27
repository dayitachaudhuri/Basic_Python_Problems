txt=input("Enter String")
pat=input("Enter substring")


M = len(pat) 
N = len(txt) 
res = 0

for i in range(N - M + 1): 
    j = 0
    for j in range(M): 
           if (txt[i + j] != pat[j]): 
                break
  
    if (j == M - 1): 
            res += 1
            
            
print(res)
