def maxvalue(arr):
    maxval=arr[0]
    
    for i in arr:
        if i>maxval:
            maxval=i
            
    return maxval
    
def main():
    arr=[5,3,1,7,2,8,1]
    print(maxvalue(arr))
    
    
main()
