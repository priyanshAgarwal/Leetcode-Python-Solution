# cook your dish here

"""
3. Longest Substring Without Repeating Characters
Solved
Medium
Topics
Companies
Hint
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


def longestSubstring(char:str)->int:

    seen = []
    result = 0

    for index, value in enumerate(char):
        if value not in seen:
            seen.append(value)
        else:
            while value in seen:
                seen.pop(0)
            seen.append(value)
        result=max(result,len(seen))
    return result



# print(longestSubstring('pwwkew'))




def get_max_lenght(s:str)->int:

    result = 0

    def calculate_substring_length(start, end)->int:
        seen = []
        for i in range(start,end+1):
            if s[i] in seen:
                break
            else:
                 seen.append(s[i])
        return len(seen)


    for i in range(len(s)):
        count = 0
        for j in range(i+1,len(s)):
            count =  calculate_substring_length(i,j)

        result = max(result,count)

    return result


print(get_max_lenght("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ "))