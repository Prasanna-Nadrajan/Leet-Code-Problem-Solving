# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(not head or not head.next):
            return head
        odd=head
        even=head.next
        t1=even
        while(odd.next!=None and t1.next !=None):
            odd.next=t1.next
            odd=odd.next
            t1.next=odd.next
            t1=t1.next
        odd.next=even
        return head
                
        
