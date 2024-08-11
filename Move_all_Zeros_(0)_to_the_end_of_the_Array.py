def shiftzeros(arr, n):
    rarr = []
    zarr = []
    
    for i in range(len(arr)):
        if arr[i] == 0:
            zarr.append(arr[i])
        else:
            rarr.append(arr[i])
    return rarr+zarr
    
def main():
    arr = [-1,-0,-2,-3,0,-5,0,-7,1]
    n = len(arr)
    print(shiftzeros(arr, n))
    
main()