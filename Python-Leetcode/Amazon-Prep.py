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

# try:
#     n = int(input("Enter the value of n:"))
#     result = fibonacci(n)
#     print(result)
# except:
#     print("Error in the code")
    
    
    
def findMax(nums:list, k:int)->list:
    result = []
    
    if k<=0:
        return -1
    
    if k>=len(nums):
        if len(nums)>0:
            result.append(max(nums))
            return result
    
    for i in range(0,len(nums)-k+1):
        localWindow = nums[i:i+k]
        # O(K)
        maxValue = max(localWindow)
        result.append(maxValue)
    return result


print(findMax([1,3,2,4,6,5], 3))