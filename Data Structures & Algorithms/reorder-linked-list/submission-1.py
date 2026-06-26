# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        fast, slow = head, head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        if prev:
            prev.next = None
        
        slow = self.reverseList(slow)

        curr = head
        while curr:
            new = slow
            slow = slow.next

            new.next = curr.next
            curr.next = new

            if new.next:
                curr = new.next
            else:
                curr.next.next = slow
                break
            
        return


    def reverseList(self, head: Optional[ListNode]):
        prev = None
        curr = head

        while curr:
            n = curr.next
            curr.next = prev
            prev = curr
            curr = n
        
        return prev