# cook your dish here

"""
1572. Matrix Diagonal Sum
Easy

Add to List

Share
Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

 

Example 1:


Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.
Example 2:

Input: mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]
Output: 8
Example 3:

Input: mat = [[5]]
Output: 5

"""

"""
First Diagonal matrix
mat[i][i]

Second Diagonal matrix
mat[i][n-1-i]

"""

# Method 1
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum_diagonal=0
        n=len(mat)
        for i in range(n):
            sum_diagonal+=mat[i][i]+mat[i][n-1-i]
        
        x = n//2
        if n%2==1:
            sum_diagonal-=mat[x][x]
        return(sum_diagonal)

# Method 2

"""
Two for loop 
if i==j or ((i+j)==n-1):
First condition is to get diagonal secong condition is to get other diagonal

Second diagonal condition ((i+j)==n-1)
"""
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n=len(mat)
        sum_diagonal=0
        for i in range(n):
            for j in range(n):
                if i==j or ((i+j)==n-1):
                    sum_diagonal+=mat[i][j]
