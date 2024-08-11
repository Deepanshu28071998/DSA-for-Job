def leftrotate1place(arr, n, l):
    rarr = []
    
    if n <= l and n >= 0:
        for i in range(n,l):
            rarr.append(arr[i])
        for j in range(0,n):
            rarr.append(arr[j])
        print(rarr)
        
    else:
        print(f"{n} is out of the length of array. The length of array is {l}.")
    
def main():
    arr = [3,5,6,8,9,1,7]
    n = int(input("Enter the nth term: "))
    l = len(arr)
    leftrotate1place(arr, n, l)
    
main()