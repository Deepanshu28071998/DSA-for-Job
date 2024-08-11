def leftrotateNplace(arr, n, l):
    rarr = []
    
    if n < l:
        lval = arr[n]
        for i in range(l):
            if i != n:
                rarr.append(arr[i])
            else:
                continue
        rarr.append(lval)
        print(rarr)
    else:
        print("You enter the list index out of range")
    
def main():
    arr = [3,5,1,2,8]
    n = int(input("Enter the nth term: "))
    l = len(arr)
    leftrotateNplace(arr, n, l)
    
main()