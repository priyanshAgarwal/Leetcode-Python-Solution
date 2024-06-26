# cook your dish here

"""
202. Happy Number
Easy

4358

626

Add to List

Share
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

 

Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
Example 2:

Input: n = 2
Output: false
 

Constraints:

1 <= n <= 231 - 1

"""

class Solution:
    def isHappy(self, n: int) -> bool:
        
        def multiply_num(n):
            total_sum=0
            while n>0:
                n, digit=divmod(n,10)
                total_sum+=digit**2
            return total_sum
    
        seen=set()   
        while n!=1 and n not in seen:
            seen.add(n)
            n=multiply_num(n)
            
        return n == 1
    
    
    
def happyNumber(num:int)->bool:
    
    def getSquare(num:int)->int:
        squareResult = 0
        
        for i in str(num):
            squareResult+=int(i)**2
        return squareResult
    
    seen = set()
    while num not in seen and num!=1:
        seen.add(num)
        num = getSquare(num=num)
        
        if num==1:
            return True
        
    return num==1
    
    
# print(happyNumber(19))
print(happyNumber(2))