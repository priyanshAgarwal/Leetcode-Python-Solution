# cook your dish here

"""

"""

def isPrime(number:int)->bool:
    divisor = set()
    for i in range(2,number):
        if number%i==0:
            divisor.add(i)
            # return False    
    return divisor

# print(isPrime(7))


def fibonacci(num:int)->list:
    
    fib = []
    fib.append(0)
    fib.append(1)
    
    for i in range(2,num):
       result = fib[i-1] +fib[i-2]
       fib.append(result)
    return fib

try:
    n = int(input("Enter the value of n:"))
    result = fibonacci(n)
    print(result)
except:
    print("Error in the code")