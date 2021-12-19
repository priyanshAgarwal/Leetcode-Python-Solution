# cook your dish here

"""
9. Palindrome Number
Easy

4617

1946

Add to List

Share
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.
 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x>=0:
            str1=str(x)
            str2=str1[::-1]
            if str1==str2:
                return True
        return False



#Method 2
from copy import copy

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x>=0:
            var_copy=copy(x)
            rev_num=0
            while x!=0:
                rev_num=rev_num*10+x%10
                x=int(x/10)
            if rev_num==var_copy: return True
        else: return False                


#Method 3
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x)==''.join(reversed(str(x))):
            return True
        else: return False
        