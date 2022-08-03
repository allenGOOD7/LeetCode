# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        temp = ListNode(0)
        result = temp
        result.next = head
        
        while temp.next and temp.next.next:
            first = temp.next
            second = temp.next.next
            
            first.next = second.next
            second.next = first
            temp.next = second
            
            temp = temp.next.next
            
        return result.next