__author__ = 'chandrashekhar'


def pattern(n, k):
    space = 0
    i = 1
    while i <= n:
        if i == 1:
            space = n+k
        if i == k+1:
            space = n-i
        print(" "*space),
        for j in range(0, i):
            print "*",
        space -= 1
        i += 1
        print("\n")
    return ""
if __name__ == '__main__':
    i = raw_input("enter initally when you want to suffle: ")
    n = raw_input("enter no of lines: ")
    print(pattern(int(n), int(i)))
