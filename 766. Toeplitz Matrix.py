# cook your dish here

"""

766. Toeplitz Matrix
Easy

1719

113

Add to List

Share
Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

 

Example 1:


Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: true
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.
Example 2:


Input: matrix = [[1,2],[2,2]]
Output: false
Explanation:
The diagonal "[1, 2]" has different elements.
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 20
0 <= matrix[i][j] <= 99
 

Follow up:

What if the matrix is stored on disk, and the memory is limited such that you can only load at most one row of the matrix into the memory at once?
What if the matrix is so large that you can only load up a partial row into the memory at once?

matrix=np.array(matrix) 

[[1,2,3,4],
[5,1,2,3],
[9,5,1,2]]

print(matrix[2:3,2:4]) This won't work if matrix is not numpy type

[[1 2]]

Take  3 row and then filter 3 and 4 column

print(matrix[0,1:4]) This won't work if matrix is not numpy type

[2 3 4]

First row ke 2,3,4 elements.

print(matrix[1][:-1]) This won't work with Numpy Matrix.

[5, 1, 2]

Print all the elements of first row except the last element.
"""

# Method 1
# Because we have to compare +1 of Matrix we run the loop with -1
class Solution(object):
	def isToeplitzMatrix(self, matrix):
		for i in range(len(matrix)-1):
			for j in range(len(matrix[0])-1):
				if matrix[i][j] != matrix[i + 1][j + 1]:
					return False
		return True


# Method 2
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        i=0
        while i+1<len(matrix):
            if matrix[i][:-1]!=matrix[i+1][1:]:
                return False
            i+=1
        return True
