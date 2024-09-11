def TOH(n, A, B,C):
    if (n == 1):
        print("Move 1 from "+A+" to "+C)
        return
    
    TOH(n - 1, A, C, B)
    print("Move "+n+" from "+A+" to "+C)
    TOH(n -1, B, A, C)

def main():
    n = int(input())
    TOH(n, 'A', 'B', 'C')

main()