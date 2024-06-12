# Python code to demonstrate 
# to find all permutation of
# a given string

# Initialising string
ini_str = "123abc%^&"

# Printing initial string
print("Initial string", ini_str)

# Finding all permutation
result = []

def permute(data, i, length): 
	if i == length: 
		result.append(''.join(data) )
	else: 
		for j in range(i, length): 
			# swap
			data[i], data[j] = data[j], data[i] 
			permute(data, i + 1, length) 
			data[i], data[j] = data[j], data[i] 
# permute(list(ini_str), 0, len(ini_str))

# Printing result
# print("Resultant permutations", str(result))


def subarraySum(nums: list[int], k: int) -> int:
	if not nums:
		return 0
	if len(nums) == 1:
		if nums[0] == k:
			return 1
		return 0
		
	# Build prefix sum:
	for i in range(1,len(nums)):
		nums[i] = nums[i-1] + nums[i]
	nums.insert(0,0)

	# itertate over prefix sum and see
	count = 0
	for i in range(len(nums)):
		for j in range(i+1, len(nums)):
			if nums[j] - nums[i] == k:     # --- I
				count += 1 
				# or return True
				# or return [i, j]
	return count
		
		# COMMENT I:
		# ------------
		# Find the prefix sum
		# iterate over the prefix sum and check if the difference between any two sums (at different stages) add up to k
		# In other words, given two sums, find out if the diffrence between them is equal to k
            
            
            
nums = [1,2,3,4,5]
k=5

# print(subarraySum(nums,k=k))




s='122231.67'
# s='1111111'
# print(compressString(s=s))

def largestNumber(s:str)->int:

	if isinstance(s,str)==True and s.isdigit()==True:
		# s=int(s)
		s=sorted(s,reverse=True)
	else:
		return -1

	return "".join(s)

print(largestNumber(s))