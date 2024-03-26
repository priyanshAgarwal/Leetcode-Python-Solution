'''
28. Find the Index of the First Occurrence in a String
Solved
Easy
Topics
Companies
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.

'''

# Two Pointer Method 

'''
Haystack  = ining
needle - ing
'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        hp=0
        np=0

        while np<len(needle) and hp<len(haystack):
            if haystack[hp] == needle[np]:
                np+=1
            else:
                hp=hp-np
                np=0
            hp+=1

        if np == len(needle):
            return hp-np
        return -1


# Sliding Window Methid
    
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)==0:
            return -1


        for i in range(0, len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)]==needle:
                return i
        
        return -1


    