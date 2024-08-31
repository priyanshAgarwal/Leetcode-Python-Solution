# cook your dish here

"""

75. Sort Colors
Solved
Medium
Topics
Companies
Hint
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
 

Constraints:

n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.
 

Follow up: Could you come up with a one-pass algorithm using only constant extra space?
"""


def sortColors1(arr:list)->list:
    colorDict = {}
    resultArray = []
    
    for i in arr:
        colorDict[i]=colorDict.get(i,0)+1
    
    
    for i in range(3):
        
        resultArray.extend([i]*colorDict[i])
        print(colorDict[i])



# Buble sort in Python 


def sortColors(arr:list)->list:
    
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j+1]<arr[j]:
                arr[j+1],arr[j] = arr[j],arr[j+1]
    
    return arr
    
nums = [2,0,2,1,1,0]
print(sortColors(nums))
