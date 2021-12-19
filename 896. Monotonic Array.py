# cook your dish here

"""
896. Monotonic Array
Easy

1277

52

Add to List

Share
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.

 

Example 1:

Input: nums = [1,2,2,3]
Output: true
Example 2:

Input: nums = [6,5,4,4]
Output: true
Example 3:

Input: nums = [1,3,2]
Output: false
Example 4:

Input: nums = [1,2,4,5]
Output: true
Example 5:

Input: nums = [1,1,1]
Output: true

"""


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = decreasing = True

        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]: 
                increasing=False
            if nums[i]<nums[i+1]:
                decreasing=False
            
        return decreasing or increasing