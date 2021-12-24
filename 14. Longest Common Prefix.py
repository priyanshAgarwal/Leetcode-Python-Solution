# cook your dish here

"""
14. Longest Common Prefix
Easy

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

#Method 1
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        shortest=min(strs,key=len)
        for i,ch in enumerate(shortest):
            for word in strs:
                if word[i]!=ch:
                    return shortest[:i]
        return shortest



#Method 2
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        str_common=""
        for i in (zip(*strs)):
            if len(set(i))==1:
                str_common+=i[0]  
            else: return str_common
        return str_common


#Method 3
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_str,max_str=min(strs),max(strs)
        
        for i,letter in enumerate(min_str):
            if letter!=max_str[i]:
                return min_str[:i]
        return min_str
