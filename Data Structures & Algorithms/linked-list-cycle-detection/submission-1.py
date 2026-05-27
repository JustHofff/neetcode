# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        f, s = head, head

        while f is not None and s is not None:
            f = f.next
            if f:
                f = f.next

            s = s.next
            if (f is not None or s is not None) and f == s:
                return True
        return False