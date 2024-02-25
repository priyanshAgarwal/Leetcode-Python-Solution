# cook your dish here

"""
1. Two Sum
Easy

26441

852

Add to List

Share
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        num_dict={}
        for i in range(0, len(nums)):
            num_dict[nums[i]]=i
        # print(num_dict)
        for i in range(0, len(nums)):
            complement = target - nums[i]
            if complement in num_dict and num_dict[complement]!=i:
                return [i, num_dict[complement]]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_with_index  = [[i,value] for i,value in enumerate(nums)]
        # nums_with_index.sort()
        nums_with_index=sorted(nums_with_index, key=lambda x:x[1])
        left,right = 0,len(nums)-1
        while left < right:
            if nums_with_index[left][1]+nums_with_index[right][1]==target:
                return [nums_with_index[left][0],nums_with_index[right][0]]
            elif nums_with_index[left][1] + nums_with_index[right][1] < target:
                left +=1
            else:
                right -=1
        return []




