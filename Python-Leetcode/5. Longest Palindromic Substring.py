# cook your dish here

"""
5. Longest Palindromic Substring
Medium
28.6K
1.7K
company
Amazon
company
Cisco
company
Apple
Given a string s, return the longest 
palindromic
 
substring
 in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.

"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)==1:
            return s

        longest=''
        for i in range(1,len(s)):
            odd_string = self.expand_around_center(s,i,i)
            if len(odd_string)>len(longest):
                longest=odd_string

            even_string = self.expand_around_center(s,i-1,i)
            if len(even_string)>len(longest):
                longest=even_string

        return longest

# My Mistakes Used If instead of While loop and condition should be left>=0 you used left>0 first element in the list is 0th Index. 
# Also you used s[left:right] you should have used s[left+1:right] because list are 0 index 

    def expand_around_center(self,s,left,right):
        while left>=0 and right<len(s) and s[left]==s[right]:
            left-=1
            right+=1
        return s[left+1:right]


