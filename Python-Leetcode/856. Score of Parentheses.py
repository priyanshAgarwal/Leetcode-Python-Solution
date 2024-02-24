# cook your dish here

"""
856. Score of Parentheses
Medium
5.4K
194
company
TikTok
company
Microsoft
company
Snapchat
Given a balanced parentheses string s, return the score of the string.

The score of a balanced parentheses string is based on the following rule:

"()" has score 1.
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.
 

Example 1:

Input: s = "()"
Output: 1
Example 2:

Input: s = "(())"
Output: 2
Example 3:

Input: s = "()()"
Output: 2
 

Constraints:

2 <= s.length <= 50
s consists of only '(' and ')'.
s is a balanced parentheses string.
"""

'''
# So you were confused ki when score of () bracket is calculated then how to add it onto () vs (())
So the thing is ()() or (()) both have a weight of 2 so that everytime a we see a closing bracket 
we are taking previous score and multiplyting by 2


"()()()()()" is 5 Since everytime bracket is opening and closing we never get to the multiplier every time we see '(' 0 is added and max(2*score,1) always get a score of 1 which get's added to the last element of stack.

"((((()))))" In this case its 10 because all the 0 [0,0,0,0,0] are added at the top of the stack and everytime we get new multiplier which get's multiplied by 2
'''


class Solution(object):
    def scoreOfParentheses(self, S):
        stack = [0] #The score of the current frame

        for x in S:
            if x == '(':
                stack.append(0)
            else:
                # We have to POP to get pop to get the last element so that we can calculate current sum using last sum. 
                score = stack.pop()
                stack[-1] = stack[-1] + max(2 * score, 1)
        return stack.pop()