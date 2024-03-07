# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev, curr = None, head

        while curr != None:

            tempPosition = curr.next
            curr.next = prev
            prev = curr
            curr = tempPosition

        return prev
        
        
#Explination, first need to define two pointers, prev and curr. Prev is equal to None and curr is the head
#We need to point the curr.next "Tail" to prev (Which is equal to None), and shift prev to curr (prev = curr). 
# Before we change the tail.next we need to store so that what is tempPosition.
