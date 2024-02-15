# cook your dish here

"""
20. Valid Parentheses
Easy
23.3K
1.6K
company
Amazon
company
Bloomberg
company
Adobe
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

"""

'''
1. Thought process Jis order me push opening bracket and usi order me closing bracket honge
2. ([ )] This can't be true
3. So dictionary ki keys push karte jao.. (Opening bracket push karte jao)
4. When you can't find the key, take the last value and check if that is equal to incoming bracket
5. If they are equal then pop it.
6. Check the length of the array in the end
'''
class Solution:
    def isValid(self, s: str) -> bool:
        array_para=[]

        dict_para ={
            '(':')',
            '{':'}',
            '[':']'
        }

        
        for bracket in s:
            if bracket in dict_para.keys():
                array_para.append(bracket)
            elif len(array_para)!=0 and dict_para[array_para[-1]]==bracket:
                array_para.pop()
            else:return False 

        return len(array_para) == 0
