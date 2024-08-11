def sortedArray(arr1, arr2):
    newarr = arr1+arr2
    arr = []
    newarr.sort()
    arr.append(newarr[0])
    
    for i in range(1, len(newarr)):
        if newarr[i] not in arr:
            arr.append(newarr[i])
        else:
            continue
    
    
    print(arr)
    
    
def main():
    arr1 = [-1,1,-2,4,-5,10]
    arr2 = [-2,-3,4,4,5,-6]
    sortedArray(arr1, arr2)
    
main()