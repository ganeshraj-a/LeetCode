# Given the head of a linked list, remove the nth node from the end of the list and return its head.

"""Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dum = ListNode(0)
        print(dum.next)
        dum.next = head 
        f = dum 
        s = dum 
        for _ in range(n+1):
            f = f.next 
        while f is not None:
            f = f.next 
            s = s.next 
        s.next = s.next.next 
        return dum.next
        
