# cook your dish here

"""
You are given a two-digit integer n. Return the sum of its digits.

Example

For n = 29, the output should be
addTwoDigits(n) = 11.

Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

A positive two-digit integer.

Guaranteed constraints:
10 ≤ n ≤ 99.

[output] integer

The sum of the first and second digits of the input number.

"""

def addTwoDigits(n):
    num1 = n / 10
    num2 = n % 10
    
    return num1 + num2


for i in range(1,5):
    print(i)


def makeArrayConsecutive2(statues):
    new_statues=[]
    for i in range(min(statues),max(statues)):
        print(i)
    return len(new_statues)

# makeArrayConsecutive2([6, 2, 3, 8])

# aa=[5, -2, 3 , 1, 2]
# print((aa[8:]))

nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(nums[-0])

def solve(A, B):
    temp = sum(A[len(A)-B:])
    max_sum = temp
    for i in range(B):
        temp = (temp - A[i-B]) + A[i]
        if temp > max_sum:
            max_sum = temp
    return (max_sum)

A = [5, -2, 3 , 1, 2]
solve(A,3)