def maxmin(arr):
    maxval=arr[0]
    minval=arr[0]
    
    for i in arr:
        if i>maxval:
            maxval=i
        if i<minval:
            minval=i
    return "Max Value",maxval,"Min value",minval
    
def main():
    arr=[4,8,1,2,9,4]
    print(maxmin(arr))
    
main()
