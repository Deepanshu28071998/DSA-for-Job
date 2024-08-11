def sortedArray(arr1, arr2):
    newarr = arr1+arr2
    arr = []
    
    arr.append(newarr[0])
    
    for i in range(1, len(newarr)):
        if newarr[i] not in arr:
            arr.append(newarr[i])
        else:
            continue
    
    arr.sort()
    print(arr)
    
    
def main():
    arr1 = [-1,1,2,4,-5]
    arr2 = [2,-3,4,-4,-5,-6]
    sortedArray(arr1, arr2)
    
main()