# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def count(head):
            c=0
            while(head is not None):
                c+=1
                head=head.next
            return c

        if head is None:
            return None
        c=count(head)
        t=c-n
        temp=head
        tt=None
        while(temp.next is not None and t!=0):
            tt=temp
            temp=temp.next
            t-=1
        if(tt is None):
            return temp.next
        tt.next=temp.next
        return head
