# cook your dish here

"""
509. Fibonacci Number
Easy

2263

240

Add to List

Share
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, 
such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

 

Example 1:

Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:

Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 3:

Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
 

Constraints:

0 <= n <= 30
"""

#Method 1 Using Memory
class Solution:
    def fib(self, n: int) -> int:
        
        def Fib_num(n):
            memo={0:0,1:1}  
            if n in memo:
                return memo[n]
            else:
                memo[n]=Fib_num(n-1)+Fib_num(n-2)
                return memo[n]
        return Fib_num(n)

#Basic Solution
class Solution:
    def fib(self, n: int) -> int:
        
        def Fib_num(n):
            if n==0:return 0
            if n==1:return 1            
            if n>=2:
                return Fib_num(n-1)+Fib_num(n-2) 
        return Fib_num(n) #Function is being called from here