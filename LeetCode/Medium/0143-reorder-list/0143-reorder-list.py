# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # first reach the mid point of the linkedlist
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # now reverse the second half of the linkedlist
        second = slow.next
        slow.next = None
        prev = None
        while second:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node
        second = prev

        # now merge the two halfs of the linkedList
        first = head
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

        return head
        