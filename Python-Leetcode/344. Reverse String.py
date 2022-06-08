# cook your dish here

"""
344. Reverse String
Easy

3189

840

Add to List

Share
Write a function that reverses a string. The input string is given as an array of characters s.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
 

Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.

"""

class Solution:
    def reverseString(self, s: List[str]) -> None:            
        left=0, right=len(s)-1

        while left<right:
            s[right], s[left]=s[left], s[right]
            # or
            s[left],s[right]=s[right],s[left]
            right-=1
            left+=1
        return s

class Solution:
    def reverseString(self, s: List[str]) -> None:
        s[:] = s[::-1]
# or could be used.       
        return s.reverse()
# s[:] = s[::-1] is required NOT s = s[::-1] because you have to edit the list inplace.
# Under the hood, s[:] = is editing the actual memory bytes s points to, 
# and s = points the variable name s to other bytes in the memory.

# arr[:] returns arr (alist[:] returns a copy of a list). 
# arr[:]=arr2 performs an inplace replacement; changing the values of arr to the values of arr2. 
# The values of arr2 will be broadcasted and copied as needed.

# arr=arr2 sets the object that the arr variable is pointing to. 
# Now arr and arr2 point to the same thing (whether array, list or anything else).
