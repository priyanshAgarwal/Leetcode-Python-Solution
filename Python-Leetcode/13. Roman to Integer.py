# cook your dish here

"""
13. Roman to Integer
Easy

2303

163

Add to List

Share
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
Example 2:

Input: s = "IV"
Output: 4
Example 3:

Input: s = "IX"
Output: 9
Example 4:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 5:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

"""

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900,
            'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        sum_roman=0
        
        for key, value in roman_map.items():
            if key in s:
                s = s.replace(key, f'+{value}')
        return eval(s)


# Method 2
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        total_sum=0
        previous=0
        for i in s[::-1]:
            current=roman_dict[i]
            if previous>current:
                total_sum-=current
            else:total_sum+=current
            previous=current
        return total_sum