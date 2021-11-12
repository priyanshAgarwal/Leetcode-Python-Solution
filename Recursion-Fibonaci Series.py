# cook your dish here

"""
#write a program to create a Fibonacci sequence and return ‘x’ values (defined by the user) 
"""

n=15
def fibonaci(n):
    fib=[0,1]
    for i in range(2,n):
        val=fib[i-1]+fib[i-2]
        fib.append(val)
    return fib

# print(fibonaci(10))

# Method 2
def fibonaci_simple(n):
    fib=[0]*n
    fib[1]=1
    for i in range(2,n):
        fib[i]=fib[i-1]+fib[i-2]

    return fib[n-1]

print(fibonaci_simple(10))



