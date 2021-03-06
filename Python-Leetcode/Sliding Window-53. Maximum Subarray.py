# cook your dish here

"""
53. Maximum Subarray
Easy

16397

768

Add to List

Share
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104 

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

"""
# Will Pass some cases
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result_arr=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                sum_values=sum((nums[i:j+1]))
                result_arr.append(sum_values)
        return max(result_arr)


# Method 1 (TLE)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:       
        ans = -inf
        for i in range(len(nums)):
            cur_sum = 0
            for j in range(i, len(nums)):
                cur_sum += nums[j]
                ans = max(ans, cur_sum)
        return ans

# Method 2
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:       
        max_sub=nums[0]
        curr_sum=0
        for i in nums:
            if curr_sum<0:
                curr_sum=0
            curr_sum+=i
            max_sub=max(max_sub,curr_sum)
        return max_sub