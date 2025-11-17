# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            

        before = None
        while slow:
            after = slow.next
            slow.next = before
            before = slow
            slow = after

        l = head
        while before:
            if l.val != before.val:
                return False
            l = l.next
            before = before.next
        return True
        
