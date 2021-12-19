# cook your dish here

"""
14. Longest Common Prefix
Easy

6220

2661

Add to List

Share
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        str_common=""
        for i in (zip(*strs)):
            if len(set(i))==1:
                str_common+=i[0]  
            else: return str_common
        return str_common