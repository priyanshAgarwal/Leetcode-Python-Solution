'''
402. Remove K Digits
Solved
Medium
Topics
Companies
Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

 

Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
 

Constraints:

1 <= k <= num.length <= 105
num consists of only digits.
num does not have any leading zeros except for the zero itself.
'''


'''
Same Number can appear K=2, num = 2220
k=2, num = 9200, Leading Zero after removal

Monotonic Increasing = 1234, remove last 3 element, In this case we would have to use inner 
while loop, beause you want to keep running the loop until you find larger value for each digit. 
Num = 1234567890, K=9. It is the perfect example. 

Num = 22, k=2 Then Number should be 0

k<=num.length

If Vs While 
num = "1234567890123"
k=9

If = "1234"

While  = "123"
'''

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i in range(len(num)):
            # We need to use while loop in case all the bigger number are righ side.
            while len(stack)>0 and k>0 and stack[-1]>num[i]:
                stack.pop()
                k-=1
            stack.append(num[i])

        while k!=0 and len(stack)>0:
            stack.pop()
            k-=1

        number = "".join(stack)
        number=number.lstrip('0')

        if len(num)>0 and number=="":
            return '0' 

        return number 
            



        


                 

        