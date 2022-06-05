# cook your dish here

"""
1047. Remove All Adjacent Duplicates In String
Easy

2351

136

Add to List

Share
You are given a string s consisting of lowercase English letters. A duplicate removal consists of 
choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the 
answer is unique.

 

Example 1:

Input: s = "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the 
only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible,
so the final string is "ca".
Example 2:

Input: s = "azxxzy"
Output: "ay"

"""

# Method 1 (Very Slow Solution, only better than 5% solution)
# Method 1
class Solution:
    def removeDuplicates(self, s: str) -> str:
        for i in s:
            if i*2 in s:
                s = s.replace(i*2, '')
        return s
                                
# Method 2
class Solution:
    def removeDuplicates(self, S: str) -> str:
        output=[]
        for ch in S:
            if output and ch==output[-1]: # So the idea is if last element in the output array is equal to 
            # current char then pop the last element from the array
                output.pop()
            else:output.append(ch)
        return ''.join(output) 
