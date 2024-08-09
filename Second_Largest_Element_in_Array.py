def SecondLargest(arr,n):
    largest = 0
    secondLargest = 0

    if arr[0] > arr[1]:
        largest = arr[0]
        secondLargest = arr[1]
    else:
        largest = arr[1]
        secondLargest = arr[0]
    
    for i in range(2,n):
        if arr[i] > largest:
            secondLargest = largest
            largest = arr[i]
        
        elif arr[i] > secondLargest:
            if arr[i] > secondLargest:
                secondLargest = arr[i]
    print("Array is",arr)
    print("Largest Element of the Array is",largest)
    print("Second Largest Element of the Array is",secondLargest)


def main():
    arr = [12, 13, 1, 10, 34, 16]
    n = len(arr)
    SecondLargest(arr,n)
main()