# cook your dish here

"""
414. Third Maximum Number
Easy

Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

 

Example 1:

Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.
Example 2:

Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.
Example 3:

Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.
"""


# Method 1
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        s = set(nums)
        if len(s) > 2:
            return sorted(s, reverse=True)[2]
        return max(s)


#Method 2
class Solution(object):
    def thirdMax(self, nums):        
        s = set(nums)
        if len(s) < 3:
            return max(s)
        else:
            s.remove(max(s))
            s.remove(max(s))
            return max(s)


#Method 3
class Solution(object):
    def thirdMax(self, nums):
        s = list(set(nums))
        s = sorted(s, reverse=True)
        if len(s) < 3:return s[0]
        else:return s[2]


#Method 4
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums=set(nums)
        max_num=max(nums)
        nums.remove(max_num)
        
        if len(nums)<2:
            return max_num
        
        nums.remove(max(nums))
        return max(nums)