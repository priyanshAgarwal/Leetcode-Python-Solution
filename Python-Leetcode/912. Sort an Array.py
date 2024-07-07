# cook your dish here

"""
912. Sort an Array
Medium
Topics
Companies
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessairly unique.

"""


def sortArray(nums: list[int]) -> list[int]:
    
    def merge(arr, left, mid, right):
        leftArr = arr[left:mid+1]
        rightArr = arr[mid+1:right+1]
        
        i,j,k = left , 0 , 0
        
        while j<len(leftArr) and k<len(rightArr):
            if leftArr[j]<=rightArr[k]:
                arr[i]=leftArr[j]
                j+=1
            else:
                arr[i]=rightArr[k]
                k+=1
            i+=1
    
        while j<len(leftArr):
            arr[i]=leftArr[j]
            j+=1
            i+=1
            
        while k<len(rightArr):
            arr[i]=rightArr[k]
            k+=1
            i+=1
        

    
    def mergeSort(arr,left,right):
        if left==right:
            return arr
        
        mid = (left + right)//2
        
        mergeSort(arr,left,mid)
        mergeSort(arr,mid+1,right)
        
        # Now we would need to merge the two array above
        merge(arr, left, mid, right)
        
        return arr
        
    resultArr = mergeSort(nums, 0, len(nums)-1)
    return resultArr

nums = [5,2,3,1]

print(sortArray(nums))