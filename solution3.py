# Write code for algorithm 3 below
# Fibonacci Sequnce?

def fibo(n):
    # This doesn't work with negatives
    if (n<=0):
        return
    elif(n==1):
        return n
    elif(n==2):
        return 1
    elif(n==3):
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
    
# print(fibo(3)) = 1
# print(fibo(4)) = 2
# print (fibo(7)) = 8
# print(fibo(9)) = 21