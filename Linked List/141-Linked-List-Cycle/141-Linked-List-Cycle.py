# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        l=[]
        temp=head
        while(temp!=None):
            if temp in l:
                return True
            else:
                l.append(temp)
            temp=temp.next
        return False
