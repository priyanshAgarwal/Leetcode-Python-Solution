# cook your dish here

"""

34. Find First and Last Position of Element in Sorted Array
Medium
Topics
Companies
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
"""

def searchRange(nums:list, target:int)->list:
    result = []
    leftIndex = binarSearch(nums,target,False)
    rightIndex = binarSearch(nums,target,True)
    result.append(leftIndex)
    result.append(rightIndex)
    return result

def binarSearch(nums,target,searchRight)->int:
    i = -1
    left = 0
    right = len(nums)-1
    
    while left<=right:
        mid = (left+right)//2
        if nums[mid]<target:
            left=mid+1
        elif nums[mid]>target:
            right=mid-1
        else:
            i = mid
            if searchRight==False:
                right=mid-1
            else:
                left=mid+1        
    return i

nums = [5,7,8,8,8,8]

print(searchRange(nums,7))