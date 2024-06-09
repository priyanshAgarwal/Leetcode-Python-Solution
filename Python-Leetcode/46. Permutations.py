# cook your dish here

"""
46. Permutations
Medium
Topics
Companies
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
 

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.


"""
def permute(nums: list[int]) -> list[list[int]]:
    def backtrack(curr):
        if len(curr) == len(nums):
            ans.append(curr[:])
            return

        for num in nums:
            if num not in curr:
                curr.append(num)
                backtrack(curr)
                curr.pop()

    ans = []
    backtrack([])
    return ans


# print(permute([1,2,3]))

from math import ceil
print(ceil(4/3))

average_row_size = 500  # In bytes
overhead_per_row = 50   # In bytes
rows_added_per_day = 1000000000


daily_growth = rows_added_per_day * average_row_size * 365

print(f"Estimated Daily Table Growth: {round(int(daily_growth)/(1048576*1024*1024),2)} Tb")

16,996.64