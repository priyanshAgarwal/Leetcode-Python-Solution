# cook your dish here

"""
206. Reverse Linked List
Easy
20.6K
403
company
Amazon
company
Microsoft
company
Apple
Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []



In case you want to create a Node class 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_linked_list(head):
    Reverses a linked list iteratively.

    Args:
        head: The head of the linked list.

    Returns:
        The head of the reversed linked list.

    if (not head) or (not head.next):
        return head
        
    p = reverse_linked_list(head.next)
    head.next.next = head
    head.next = None
    return p
    # return prev  # prev becomes the new head

# Example usage
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

reversed_head = reverse_linked_list(head)

while reversed_head:
    print(reversed_head.data, end=" -> ")
    reversed_head = reversed_head.next

print("None")


"""

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr is not None:
            next_element = curr.next 
            curr.next = prev
            prev = curr # All the values itteratively will be added into this variable
            curr=next_element # All the next values are added in this variable.  
        
        return prev
