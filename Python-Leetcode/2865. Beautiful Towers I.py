# cook your dish here

"""
2865. Beautiful Towers I
Medium
Topics
Companies
Hint
You are given an array heights of n integers representing the number of bricks in n consecutive towers. Your task is to remove some bricks to form a mountain-shaped tower arrangement. In this arrangement, the tower heights are non-decreasing, reaching a maximum peak value with one or multiple consecutive towers and then non-increasing.

Return the maximum possible sum of heights of a mountain-shaped tower arrangement.

Example 1:

Input: heights = [5,3,4,1,1]

Output: 13

Explanation:

We remove some bricks to make heights = [5,3,3,1,1], the peak is at index 0.

Example 2:

Input: heights = [6,5,3,9,2,7]

Output: 22

Explanation:

We remove some bricks to make heights = [3,3,3,9,2,2], the peak is at index 3.

Example 3:

Input: heights = [3,2,5,5,2,3]

Output: 18

Explanation:

We remove some bricks to make heights = [2,2,5,5,2,2], the peak is at index 2 or 3.

"""



from typing import List

def maximumSumOfHeights(heights:List[int])->int:
    
    n = len(heights)
    globalMax = 0
    for i in range(n):
        heightCopy = heights.copy()

        maxIndex = i
    
        # Iteration for Left
        for i in range(maxIndex-1,-1,-1):
            heightCopy[i]=min(heightCopy[i],heightCopy[i+1])
        
        
        # Iteration for Right
        for i in range(maxIndex+1,n,1):
            heightCopy[i]=min(heightCopy[i],heightCopy[i-1])
         
        localMax = sum(heightCopy)
        
        globalMax=max(globalMax,localMax)
    return globalMax
    
    
nums = [3,3,3,9,2,2,4,7]
nums = [3,2,5,5,2,3]


test_cases = [
    {"heights": [5, 3, 4, 1, 1], "expected_output": 13},
    {"heights": [6, 5, 3, 9, 2, 7], "expected_output": 22},
    {"heights": [3, 2, 5, 5, 2, 3], "expected_output": 18},
    {"heights": [2, 4, 5, 2, 5, 5, 2, 1, 1, 3], "expected_output": 23}
]


def run_tests(test_cases, max_mountain_sum_func):  # Pass your function as an argument
    for case in test_cases:
        result = max_mountain_sum_func(case["heights"])  # Call your Function

        if result == case["expected_output"]:
            print(f"Test passed for heights={case['heights']}")
        else:
            print(f"Test failed for heights={case['heights']}. Expected: {case['expected_output']}, Got: {result}")

run_tests(test_cases, maximumSumOfHeights)  # Pass your function

# print(maximumSumOfHeights(nums))