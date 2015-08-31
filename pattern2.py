__author__ = 'chandrashekhar'


def pattern2(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print i,
        print "\n"

if __name__ == '__main__':
    print pattern2(int(raw_input("enter the no of lines: ")))
//this for stash
#git checkout
