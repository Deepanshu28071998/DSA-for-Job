def minvalue(arr):
    minval=arr[0]
    
    for i in arr:
        if i<minval:
            minval=i
    return minval
    
def main():
    arr=[2,8,4,1,7]
    print(minvalue(arr))
    
main()
