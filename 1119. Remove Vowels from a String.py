# cook your dish here

"""
1119. Remove Vowels from a String

Given a string s, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.

Example 1:

Input: s = "leetcodeisacommunityforcoders"
Output: "ltcdscmmntyfrcdrs"
Example 2:

Input: s = "aeiou"
Output: ""

"""


# Method 1
class Solution(object):
    def removeVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        new_sttr=[]
        vowels=set('aeiou')
        for i in s:
            if i not in vowels: #if i not in 'aeiou' can also be used but using set is lot better:
                new_sttr.append(i)
        return ''.join(i for i in new_sttr)