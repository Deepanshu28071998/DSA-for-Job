def Rope_Cutting(n, a, b, c):
    if n == 0:
        return 0
    if n < 0:
        return -1
    res = max(Rope_Cutting(n -a, a, b, c), Rope_Cutting(n - b, a, b, c), Rope_Cutting(n - c, a, b, c))

    if res == -1:
        return -1
    return res + 1

def main():
    n = int(input("Enter the value of n: "))
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    c = int(input("Enter the value of c: "))

    print(Rope_Cutting(n, a, b, c))

main()