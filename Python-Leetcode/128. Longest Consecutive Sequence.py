# cook your dish here

"""
128. Longest Consecutive Sequence
Solved
Medium
Topics
Companies
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

# This is Brute Force

def longestConsecutive(nums: list[int]) -> int:
    
    maxLength = 0 
    
    for num in nums:
        currentNumber = num
        currentStreak = 1
        
        while currentNumber+1 in nums:
            currentNumber+=1
            currentStreak+=1
        
        
        maxLength = max(maxLength,currentStreak)
        
    
    return maxLength


nums = [100,4,200,1,3,2]


print(longestConsecutive(nums))