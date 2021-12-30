# cook your dish here

"""
217. Contains Duplicate
Easy

Share
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

"""

#Method 1
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_dict={}
        for i in nums:
            num_dict[i]=num_dict.get(i,0)+1
            
        for key,value in num_dict.items():
            if value>1:
                return True
        return False

#Method 2
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        arr=(set(nums))
        if len(arr)<len(nums):
            return True
        else:
            return False
