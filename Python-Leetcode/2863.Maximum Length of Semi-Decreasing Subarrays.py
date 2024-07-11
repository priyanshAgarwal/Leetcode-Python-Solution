# cook your dish here

"""
2863. Maximum Length of Semi-Decreasing Subarrays
Medium
Topics
Companies
Hint
You are given an integer array nums.

Return the length of the longest semi-decreasing subarray of nums, and 0 if there are no such subarrays.

A subarray is a contiguous non-empty sequence of elements within an array.
A non-empty array is semi-decreasing if its first element is strictly greater than its last element.
 

Example 1:

Input: nums = [7,6,5,4,3,2,1,6,10,11]
Output: 8
Explanation: Take the subarray [7,6,5,4,3,2,1,6].
The first element is 7 and the last one is 6 so the condition is met.
Hence, the answer would be the length of the subarray or 8.
It can be shown that there aren't any subarrays with the given condition with a length greater than 8.
Example 2:

Input: nums = [57,55,50,60,61,58,63,59,64,60,63]
Output: 6
Explanation: Take the subarray [61,58,63,59,64,60].
The first element is 61 and the last one is 60 so the condition is met.
Hence, the answer would be the length of the subarray or 6.
It can be shown that there aren't any subarrays with the given condition with a length greater than 6.
Example 3:

Input: nums = [1,2,3,4]
Output: 0
Explanation: Since there are no semi-decreasing subarrays in the given array, the answer is 0.
"""

import multiprocessing
import numpy 
import numpy as np 

def maxSubarrayLength1(nums: np.ndarray) -> int:
    globalMax = 0
    for  i in range(0,len(nums)):
        for j in range(i+1, len(nums)):
            if nums[j]<nums[i]:
                globalMax = max(globalMax, j - i + 1)

    return globalMax



from typing import List

def maxSubarrayLength(nums: List[int]) -> int:
    n = len(nums)

    # Build prefix max array (equivalent to the C++ vector)
    prefix_max = [0] * n
    prefix_max[0] = nums[0]
    for i in range(1, n):
        prefix_max[i] = max(prefix_max[i - 1], nums[i])

    # Find farthest possible left index for each right index (j)
    max_length = 0
    for j in range(n):
        left, right = 0, j - 1  # Binary search range
        while left < right:
            mid = left + (right - left) // 2  # Integer division for midpoint
            if prefix_max[mid] <= nums[j]:
                left = mid + 1
            else:
                right = mid
        # Check if a semi-decreasing subarray exists
        if left < j and nums[left] > nums[j]: 
            max_length = max(max_length, j - left + 1)

    return max_length

nums = [57,55,50,60,61,58,63,59,64,60,63]
print(maxSubarrayLength(nums))
 
# nums = numpy.array(nums)

# def process_chunk(data_chunk):
#     print(f"Result is: {maxSubarrayLength(nums)}")
#     # Your processing logic here

# if __name__ == '__main__':
#     data = nums
#     num_processes = multiprocessing.cpu_count()  # Use all available cores

#     with multiprocessing.Pool(processes=num_processes) as pool:
#         pool.map(process_chunk, data)
