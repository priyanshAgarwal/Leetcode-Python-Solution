# cook your dish here

"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0 
        for start in range(len(nums)):
            for end in range(start+1,len(nums)+1):
                sum = 0
                for i in range(start, end):
                    sum += nums[i]
                if sum == k:
                    count += 1
                  
        return count 
	
O(N^3), O(1)

Approach 2 : Using Cumulative sum  (Time limit exceeded )

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count =0 
        sum = [0 for _ in range(len(nums)+1)]
        for i in range(1, len(nums)+1):
            sum[i] = sum[i -1] + nums[i]
        for start in range(len(nums)):
            for end in range(start +1, len(nums)+1):
                if sum[end] - sum[start] == k:
                    count += 1 
        return count 

O(N^2), O(N)
 
Approach 3: Without Space. (Time Limit Exceeded)

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        for start in range(len(nums)):
            sum = 0 
            for end in range(start, len(nums)):
                sum += nums[end]
                if sum == k:
                    count += 1 
        return count 
		
O(N^2), O(1)

Approach 4: Using Hashmap (Accepted)

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = s = 0
        Map = {}
        Map[0] = 1 
        for i in range(len(nums)):
            s += nums[i]
            if s - k in Map:
                count += Map.get(s-k)
            Map[s] = Map.get(s,0) +1 
        return count 
		
O(N),O(N) 
"""

