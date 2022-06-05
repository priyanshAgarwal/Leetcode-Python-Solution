# cook your dish here

"""
1351. Count Negative Numbers in a Sorted Matrix
Easy


Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, 
return the number of negative numbers in grid.


Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0
Example 3:

Input: grid = [[1,-1],[-1,-1]]
Output: 3
Example 4:

Input: grid = [[-1]]
Output: 1
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
-100 <= grid[i][j] <= 100

"""

#Method 1
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count=0
        for row in grid:
            for element in row:
                if element<0:count+=1
        return count



#Method 2
import numpy as np

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count=0
        grid_list=np.array(grid).flatten()
        for i in grid_list:
            if i<0:count+=1
        return count