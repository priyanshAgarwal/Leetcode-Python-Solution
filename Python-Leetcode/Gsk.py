
import math
def count_adjecent_words(words):

    pnt1=0
    pnt2=1
    counter = 0
    words=words+'0'
    while pnt1<len(words) and pnt2<len(words):
        if words[pnt1]!=words[pnt2]:
            pnt1+=1
            pnt2+=1
        else:
            if words[pnt1]==words[pnt2]:
                while words[pnt1]==words[pnt2] and pnt2<len(words):
                    pnt2+=1
                counter += pnt2-pnt1
                pnt1 = pnt2-1


    return counter



# print(count_adjecent_words('abaaabaaa'))

# print(count_adjecent_words('abaaab'))



# def get_scores(char:str)->int:
#   result = 0
#   value = []
#   for letter in char:
#      value.append(ord(letter)-ord('a'))
#   for i in range(1,len(value)):
#      result += abs(value[i-1]-value[i])
#   return result


# print(get_scores('bat'))


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