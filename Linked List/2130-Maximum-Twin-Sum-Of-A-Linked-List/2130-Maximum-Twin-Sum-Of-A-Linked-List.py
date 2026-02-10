# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        p1,p2=head,head
        while(p2 and p2.next):
            p1=p1.next
            p2=p2.next.next
        prev=None
        current=p1
        while current:
            nn=current.next
            current.next=prev
            prev=current
            current=nn
        m=0
        t1,t2=head,prev
        while(t1.next and t2):
            m=max(m,t1.val+t2.val)
            t1=t1.next
            t2=t2.next
        return m
