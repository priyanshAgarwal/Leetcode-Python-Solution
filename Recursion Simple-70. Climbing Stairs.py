# cook your dish here

"""
70. Climbing Stairs
Easy

8952

266

Add to List

Share
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step



"""

#Simple Recursion With No Memory
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        def climb(n):
            if n>2:
                return climb(n-1) + climb(n-2)
            elif n==1:return 1
            elif n==2:return 2
        return climb(n)



# With Memory
class Solution(object):
    def climbStairs(self, n):
        def climb(n):
            
            memo={}
            memo[1]=1
            memo[2]=2
            
            if n in memo:
                return memo[n]
            else:
                memo[n]=climb(n-1) + climb(n-2)
                return memo[n]
        return climb(n)
