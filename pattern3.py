__author__ = 'chandrashekhar'


def pattern(n, k):
    space = 0
    i = n
    while i > 0:
        if i != k:
            print " "*space,
        else:
            space += 2*k
            print " "*space,
        for j in range(0, i):
            print "*",
        space += 1
        i -= 1
        print("\n")
    return ""
if __name__ == "__main__":
    i = raw_input("enter when you want to suffle: ")
    n = raw_input("enter no of lines: ")
    print pattern(int(n), int(i))
