__author__ = 'chandrashekhar'


def pattern():
    a = 1
    for i in range(1, 5):
        for j in range(1, i + 1):
            print a,
            a += 1
        print("\n")
    return ""

print(pattern())

//pattern
//this is for stash
