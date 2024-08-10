def leftrotate1place(arr, n):
    rarr = []
    for i in range(1,n):
        rarr.append(arr[i])
    rarr.append(arr[0])
    print(rarr)

def main():
    arr = [1, 2, 3, 4, 5, 6]
    n = len(arr)
    leftrotate1place(arr, n)

main()