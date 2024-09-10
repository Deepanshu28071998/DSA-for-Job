def subsets(s, curr, i):
    if (i == len(s)):
        print(curr)
        return
    subsets(s, curr, i+1)
    subsets(s, curr+s[i], i+1)

def main():
    s = str(input())
    curr = ""
    i = 0

    subsets(s, curr, i+1)
    subsets(s, curr+s[i], i+1)
main()