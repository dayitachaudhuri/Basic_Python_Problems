#RECURSIVE

def binSearchrec(arr, minim, maxim, x): 

    if minim<=maxim and minim>=0:
        
        mid = (maxim+minim)//2
  
        if arr[mid] == x: 
            return mid 

        elif arr[mid] < x: 
            return binSearchrec(arr, mid+1, maxim, x) 
  
        else: 
            return binSearchrec(arr, minim, mid-1, x) 
  
    else:  
        return -1
  



#ITERATIVE

def binSearchit(arr, minim, maxim, x): 
  
    while minim<=maxim: 
  
        mid = (minim+maxim)//2
        
        if arr[mid] == x: 
            return mid 

        elif arr[mid] < x: 
            minim = mid + 1
  
        else: 
            maxim = mid - 1
            
    return -1


#CALLING THE FUNCTION

arr = [ 2, 5, 8, 11, 88 ] 
x = 7
  
print(binSearchrec(arr, 0, len(arr)-1, x)) 
print(binSearchit(arr, 0, len(arr)-1, x)) 
