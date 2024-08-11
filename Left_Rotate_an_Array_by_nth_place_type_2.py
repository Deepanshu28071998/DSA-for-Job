def leftrotateNplace(arr, n, l):
    if n < l:
        shift_val = arr.pop(n)
        arr.insert(l-1,shift_val)
        print(arr)
    else:
        print("You not enter the number under the length of array.")
def main():
    arr = [3,2,5,7,1,8]
    n = int(input("Enter the nth place: "))
    l = len(arr)
    leftrotateNplace(arr,n,l)
    
main()