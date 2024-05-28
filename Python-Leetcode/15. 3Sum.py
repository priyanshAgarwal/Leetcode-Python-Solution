# cook your dish here

"""
15. 3Sum
Solved
Medium
Topics
Companies
Hint
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = set()

        for i in range(len(nums)):
            first_idx = i

            second_idx = first_idx+1
            third_idx = len(nums)-1

            while second_idx<third_idx:
                sum_num = nums[first_idx]+nums[second_idx]+nums[third_idx]

                if sum_num<0:
                    second_idx+=1
                elif sum_num>0:
                    third_idx-=1
                else:
                    # You were so supid that you forgot to increase and decrease second and third pointer.. 
                    result.add((nums[first_idx],nums[second_idx],nums[third_idx]))
                    second_idx+=1
                    third_idx-=1
        return result



def threeSum(nums:list)->list:
    
    result = set()
    nums.sort()
    
    
    for i in range(1,len(nums)):
        firstIndex = i
        secondIndex = firstIndex+1
        
        thirdIndex = len(nums)-1
        
        while secondIndex<thirdIndex:
            localSum = nums[firstIndex]+nums[secondIndex]+nums[thirdIndex]
            if localSum<0:
                thirdIndex-=1
            elif localSum>0:
                secondIndex+=1
            else:
                result.add((nums[firstIndex],nums[secondIndex],nums[thirdIndex]))
                secondIndex+=1
                thirdIndex-=1        
                        
    return result

nums = [-1,0,1,2,-1,-4]

print(threeSum(nums))