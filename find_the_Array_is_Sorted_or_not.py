def sortArray(arr, n):

    for i in range(n-1):
        if arr[i] <= arr[i+1]:
            return True
        else:
             return False
    return True


def main():
    arr = [5, 2, 8, 1, 9]
    n = len(arr)
    print(sortArray(arr, n))
main()