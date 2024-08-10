def uniqueEle(arr, n):
    newarr = []
    newarr.append(arr[0])

    for i in range(1,n):
        if arr[i] not in newarr:
            newarr.append(arr[i])
        #     return newarr
        # else:
        #     return newarr
    print(newarr)

def main():
    arr = [-1, -2,-3, -3, -3, -5, -4, -6, -4, -5, -6, -1, -4]
    n = len(arr)
    uniqueEle(arr, n)

main()