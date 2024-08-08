def BubbleSort(arr,n):
    print(arr)
    for j in range(n-1):
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    print(f"Sorted Array:",arr)



def main():
    arr = [2,5,1,8,3,8,6,0,4,1,2,3,4,5,6,3,4,2,1]
    n = len(arr)
    BubbleSort(arr,n)

main()
