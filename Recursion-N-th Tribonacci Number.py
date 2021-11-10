# cook your dish here

"""
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

 

Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
Example 2:

Input: n = 25
Output: 1389537
 

Constraints:

0 <= n <= 37
The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.

"""

# My Solution (Method 1)
class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        elif n==1 or n==2:
            return 1
        else:        
            n0=0
            n1=1
            n2=1
            list_seq=[0,1,1]
            n-=2
            while n!=0:
                nth=n0+n1+n2
                list_seq.append(nth)
                n0=n1
                n1=n2
                n2=nth
                n-=1
            return list_seq[-1]



#Method 2 (Awesome Method)

class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0:
            return 0
        elif n==1 or n==2:
            return 1
        else:
            nums=[0,1,1]
            for i in range(n-2):
                nums.append(nums[-1]+nums[-2]+nums[-3])
            return nums[-1]

