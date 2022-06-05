# cook your dish here

"""
283. Move Zeroes
Easy

7267

204

Add to List

Share
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you minimize the total number of operations done?

"""

# Method 1
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for _ in range(nums.count(0)):
            nums.remove(0)
            nums.append(0)
            
#Method 2
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[k]=nums[i]
                k+=1
        while k < len(nums):
            nums[k] = 0
            k += 1
            