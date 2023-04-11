# Write code for algorithm 1 below
# Direct recursion.
def postitive(n):
    if n==0:
        return
    else:
        print(n)
        postitive(n-1)

# postitive(5)