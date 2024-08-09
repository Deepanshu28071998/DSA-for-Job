def is_sorted(arr):
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))

arr = [2,5,7]
print(is_sorted(arr))