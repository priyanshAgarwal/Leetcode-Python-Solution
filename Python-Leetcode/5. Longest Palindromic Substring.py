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


def longestPalindrome(s: str) -> str:
    if len(s)==1:
        return s

    longest=''
    for i in range(1,len(s)):
        odd_string = expand_around_center(s,i,i)
        if len(odd_string)>len(longest):
            longest=odd_string

        even_string = expand_around_center(s,i-1,i)
        if len(even_string)>len(longest):
            longest=even_string

    return longest

# My Mistakes Used If instead of While loop and condition should be left>=0 you used left>0 first element in the list is 0th Index. 
# Also you used s[left:right] you should have used s[left+1:right] because list are 0 index 

def expand_around_center(s,left,right):
    while left>=0 and right<len(s) and s[left]==s[right]:
        left-=1
        right+=1
        # We are doing this so that we can expand around center
    return s[left+1:right]

s = "bb"

print(longestPalindrome(s))  # Output: "bab" or "aba"




# Brute Force
def longestPalindrome2(s: str) -> str:
    maxString = ""

    def checkPalindrome(checkStr: str) -> str:
        left, right = 0, len(checkStr) - 1

        while left < right:  
            if checkStr[left] != checkStr[right]:  # Compare characters correctly
                return ""  # Early exit if not a palindrome
            left += 1  # Move towards the center
            right -= 1 
        return checkStr  # Return the whole string if it's a palindrome
    
    if not s:
        return s  #Handle an empty string
    if len(s)==1:
        return s

    for i in range(len(s)):
        for j in range(i+1, len(s) + 1): # Add 1 to end index for inclusive range
            checkStr = checkPalindrome(s[i:j])
            if len(checkStr) > len(maxString):
                maxString = checkStr
            
    return maxString

            
    