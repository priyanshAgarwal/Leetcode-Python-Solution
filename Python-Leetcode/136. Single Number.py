# cook your dish here

"""
136. Single Number
Easy

7843

276

Add to List

Share
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1

"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_dict={}
        for i in nums:
            num_dict[i]=num_dict.get(i,0)+1
        
        for key,value in num_dict.items():
            if value==1:
                return(key)