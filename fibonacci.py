__author__ = 'chandrashekhar'
parents,babies=(0,1)
while babies<5:
    print 'This generation has {0} babies'.format(babies)
    parents,babies=(babies,parents+babies)
// This is RAKA..