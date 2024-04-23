'''

347. Top K Frequent Elements
Medium
16.8K
624
company
Facebook
company
Amazon
company
Apple
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_map=dict()
        for i in nums:
            num_map[i]=num_map.get(i,0)+1
        num_map=dict(sorted(num_map.items(), key=lambda x:x[1], reverse=True))
        result=[]
        for i, key in enumerate(num_map):
            if i+1<=k:
                result.append(key)
        return result
    


# This is bucket sort approach, This is O(N) because you are only itterating each element once. 
    
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_num = Counter(nums)

        # For loop start at 0 and 3(eg) but we want 4 because array have 4 elements at max 
        freq = [[] for i in range(len(nums)+1)]


        for i, (key, value) in enumerate(dict_num.items()):
            freq[value].append(key)

        result = []
        for i in range(len(freq)-1,-1,-1):
            for j in freq[i]:
                result.append(j)

                if len(result)==k:
                    return result


# This is Heap Approach, This is O(K*Log(N)). 

from collections import Counter
from heapq import heapify

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # [1,1,1,2,3,2]
        dict_num = Counter(nums)
        # {1:3,2:2,3}
        heap=[] 
        for key,value in dict_num.items():
            # Because in Python we have min heap
            heap.append([-value,key])
        # O(n)
        heapify(heap)

        result=[]
        # K * Log*n
        for i in range(k):
            # Heappop log*n
            result.append(heappop(heap)[1])
        return result



                






                




                


