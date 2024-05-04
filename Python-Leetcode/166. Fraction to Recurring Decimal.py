'''

166. Fraction to Recurring Decimal
Medium
Topics
Companies
Hint
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

If multiple answers are possible, return any of them.

It is guaranteed that the length of the answer string is less than 104 for all the given inputs.

 

Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"
Example 2:

Input: numerator = 2, denominator = 1
Output: "2"
Example 3:

Input: numerator = 4, denominator = 333
Output: "0.(012)"
 

Constraints:

-231 <= numerator, denominator <= 231 - 1
denominator != 0
'''

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        
        if denominator==0:
            return '0'
        if numerator==0:
            return '0'

        if numerator%denominator==0:
            return str(numerator//denominator)

        result =[]
        sign = ""
        if numerator<0 or denominator<0:
            result.append("-")

        que = numerator//denominator
        result.append(str(que))
        result.append(".")
        q_dict = {}

        while True:
            remainder = numerator%denominator
            numerator = remainder*10
            q = numerator//denominator

            if remainder==0:                
                for key, value in q_dict.items():
                    result.append(str(value))
                break

            if numerator not in q_dict:
                q_dict[numerator]=q
            elif numerator in q_dict:
                result.append('(')
                for key, value in q_dict.items():
                    result.append(str(value))
                result.append(')')
                break
                
        return "".join(result)






        

            
