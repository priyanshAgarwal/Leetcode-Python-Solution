# cook your dish here

""" 
9. Palindrome Number
Easy

Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

 

Example 1:

Input: x = 121
Output: true
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Example 4:

Input: x = -101
Output: false
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?
"""

# Method 1
"""
Simple method reverse a number and check with the original number
"""
from copy import copy

class Solution1:
    def isPalindrome(self, x: int) -> bool:
        if x>=0:
            var_copy=copy(x)
            rev_num=0
            while x!=0:
                rev_num=rev_num*10+x%10
                x=int(x/10)
            if rev_num==var_copy: return True
        else: return False                


# Method 2 Using String Manupulation 
class Solution2:
    def isPalindrome(self, x: int) -> bool:
        if str(x)==str(x)[::-1]:
            return True
        else: return False 

# Method 3
class Solution3:
    def isPalindrome(self, x: int) -> bool:
      if str(x)==''.join(reversed(str(x))):
        return True
      else:
        return False