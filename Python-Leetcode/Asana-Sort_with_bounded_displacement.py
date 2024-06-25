# cook your dish here

"""

"""

# Function to sort an array using
# insertion sort


import heapq

def sort_with_bounded_displacement(arr, k):
    """
    Sorts an array where the maximum displacement of any element is bounded by k.
    """
    n = len(arr)

    # Min-heap to store elements and their original indices within the window
    heap = [(arr[i], i) for i in range(min(n, k + 1))]
    heapq.heapify(heap) 

    result = []

    for i in range(n):
        # Find the smallest element in the current window
        num, idx = heapq.heappop(heap)  
        result.append(num)

        # If we're not at the end of the array, add the next element to the window
        if i + k + 1 < n:
            heapq.heappush(heap, (arr[i + k + 1], i + k + 1)) 

    return result

  
    
num =  [6, 5, 3, 2, 8, 10, 9]

print(sort_with_bounded_displacement(num,3))