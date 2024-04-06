# cook your dish here

"""
876. Middle of the Linked List
Solved
Easy
Topics
Companies
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
Example 2:


Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 

Constraints:

The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Check if list is not empty or not circular

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head==None:
            return -1 
        count = 0
        # we need a node to keep track of head, because you don't want to update head
        node = head 
        while node != None:
            count +=1
            node = node.next        
        middle = count // 2
        node = head
        for i in range(middle):
            node = node.next
        return node  

        

        