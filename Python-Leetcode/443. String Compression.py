# Cook your dish here

'''
443. String Compression
Medium
Topics
Companies
Hint
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
Example 2:

Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.
Example 3:

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
 

Constraints:

1 <= chars.length <= 2000
chars[i] is a lower

'''

# Reason we can't do this with counter because Counter won't maintain the sequence.. 

# Case 1 - ["c","c","b","b","a","c","a"]
# Case 2 - ["c","c","c","b","b","a","a"]

# Both are same cases for Counter and result will be same, 

def compress(chars: list[str]) -> int:
    stack = []
    write = 0  # Index to write in the original array

    for char in chars + ['']:  # Sentinel to process the last group
        if stack and char != stack[-1]:  # New character found
            pop_count = 0
            while stack and char != stack[-1]:
                stack.pop()
                pop_count += 1

            if pop_count > 1:
                for digit in str(pop_count):
                    chars[write] = digit
                    write += 1

            stack.append(char)  # Push the new character 
        else:
            stack.append(char) 

    # Final write from the stack 
    while stack:
        chars[write] = stack.pop()
        write += 1

    return write  # New length of the array

chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
result = compress(chars)

print(result)

# But this code will fail for above usecase. 

class Solution:
  def compress(self, chars: List[str]) -> int:
    ans = 0
    i = 0
    result = []
    while i < len(chars):
    letter = chars[i]
    count = 0
    while i < len(chars) and chars[i] == letter:
        count += 1
        i += 1
    chars[ans] = letter
    result.append(letter)
    ans += 1
    if count > 1:
        for c in str(count):
        chars[ans] = c
        result.append(c)
        ans += 1
    print(result)
    return len(result)