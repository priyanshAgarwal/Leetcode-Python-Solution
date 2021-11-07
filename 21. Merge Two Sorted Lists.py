# cook your dish here

"""
21. Merge Two Sorted Lists
Easy

Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

Example 1:s
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: l1 = [], l2 = []
Output: []

Example 3:
Input: l1 = [], l2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both l1 and l2 are sorted in non-decreasing order.


https://leetcode.com/problems/merge-two-sorted-lists/discuss/759870/Python3-Solution-with-a-Detailed-Explanation-dummy-explained
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
        dummy = temp = ListNode(0)
        # print(dummy)
        # print(cur)
        while l1 and l2:
            if l1.val<l2.val:
                temp.next=l1
                l1=l1.next
            else: 
                temp.next=l2 
                l2=l2.next
            temp=temp.next
        temp.next = l1 or l2
        return dummy.next

# Method 2
class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


l1=ListNode(val=1)
l1.next=ListNode(val=2,next=ListNode(val=4,next=None))

l2=ListNode(val=1)
l2.next=ListNode(val=3,next=ListNode(val=4,next=None))

print(l1,l2)
aa=Solution()
sol_tu=aa.mergeTwoLists(l1,l2)
while sol_tu:
    print(sol_tu.val)
    sol_tu=sol_tu.next
