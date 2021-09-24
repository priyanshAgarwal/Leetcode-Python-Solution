# cook your dish here

"""
14. Longest Common Prefix

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

class Solution(object):
    def longestCommonPrefix(self, strs):
        result = ""    
        for n in (zip(*strs)):
            """
            print(n)
            (u'f', u'f', u'f')
            (u'l', u'l', u'l')
            (u'o', u'o', u'i')

            print(set(n))
            set([u'f'])
            set([u'l'])
            set([u'i', u'o'])

            So we only take all the values where set len=1
            """

            if len(set(n))==1:
                result+=n[0]  
            else: return result # This returnis to break when we have exausted all the sinle len sets.  
        return result # This return is important if intial strs in empty