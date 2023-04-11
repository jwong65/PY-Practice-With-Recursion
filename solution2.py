# Write code for algorithm 2 below
# o has to be the n 
def counts_up(n, o= 1):
    if (o>n):
        return
    else:
        print (o)
        # So this would print 1 at first
        counts_up(n, o+1)
        # Now there's a not a default argument that increases