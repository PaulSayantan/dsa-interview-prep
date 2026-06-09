# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverses a singly-linked list iteratively and in-place.
        
        Thought Process:
        Instead of allocating new nodes or copying values, we iterate through
        the list and flip the 'next' pointer of each node to point backward.
        We track 'prev' to know where to point backward to, and cache 'curr.next'
        in a temporary variable so we don't lose the rest of the list.
        """
        prev = None
        curr = head
        
        while curr is not None:
            # Step 1: Save the rest of the original list
            next_node = curr.next  
            
            # Step 2: Reverse the current node's pointer
            curr.next = prev       
            
            # Step 3: Move the 'prev' tracking pointer forward to the current node
            prev = curr            
            
            # Step 4: Advance 'curr' to the node we saved in Step 1
            curr = next_node       
            
        # When curr becomes None, prev points to the new head of the reversed list
        return prev
