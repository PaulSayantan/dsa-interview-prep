# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = curr = ListNode(-999)
        c1, c2 = l1, l2
        while c1 != None and c2 != None:
            add = c1.val + c2.val + carry
            carry = add // 10
            add = add % 10
            
            node = ListNode(val=add)
            curr.next = node
            curr = curr.next

            c1 = c1.next
            c2 = c2.next

        while c1 != None:
            add = c1.val + carry
            carry = add // 10
            add = add % 10
            
            node = ListNode(val=add)
            curr.next = node
            curr = curr.next

            c1 = c1.next

        while c2 != None:
            add = c2.val + carry
            carry = add // 10
            add = add % 10
            
            node = ListNode(val=add)
            curr.next = node
            curr = curr.next

            c2 = c2.next

        if carry == 1:
            node = ListNode(val=1)
            curr.next = node

        return head.next


