# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """
    =====================================================================================
    INTUITION:
    The problem asks us to add two numbers represented by linked lists in reverse order.
    Because the digits are stored in reverse, the head of the linked list contains the 
    least significant digit (the ones place). This is highly advantageous because standard 
    addition naturally starts from the least significant digit and moves to the most 
    significant, carrying over any excess (carry >= 10) to the next position.
    
    APPROACH:
    We can simulate primary school addition digit-by-digit. We will traverse both 
    linked lists simultaneously, summing the corresponding digits along with any carry 
    from the previous step. 
    
    SOLUTION TECHNIQUES APPLIED:
    1. Dummy Head Node: A classic linked list technique. By initializing a dummy node 
       at the start, we avoid writing special edge-case logic for the very first node 
       of our result list. We build the list off `dummy_head.next`.
    2. Unified `while` Loop: Instead of writing separate loops for when `l1` and `l2` 
       are equal length, and then extra loops for the remainders of `l1` or `l2`, we 
       use a single loop `while l1 or l2 or carry`. This elegantly handles lists of 
       different lengths and the final leftover carry.
    3. Null-Coalescing Logic: If one list is shorter, we treat its missing nodes as `0`.
    4. Modulo & Integer Division: Efficiently separates the sum into the digit to keep 
       (`sum % 10`) and the carry to pass on (`sum // 10`).
    =====================================================================================
    """
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # TECHNIQUE 1: Dummy Node. 
        # This acts as a placeholder to anchor the start of our new list.
        # We also need a 'current' pointer to actively build the list node by node.
        dummy_head = ListNode(0)
        current = dummy_head
        
        # Initialize the carry to 0 before we start adding.
        carry = 0
        
        # TECHNIQUE 2: Unified Loop.
        # Continue iterating as long as there are nodes left in l1, nodes left in l2, 
        # OR a non-zero carry that still needs to be added as a final node (e.g., 8 + 5 = 13).
        while l1 or l2 or carry:
            
            # TECHNIQUE 3: Null-Coalescing/Default values.
            # Extract the values from the current nodes. If we have reached the end 
            # of one list but not the other, substitute 0 for the missing value.
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the total sum for the current place value.
            total = val1 + val2 + carry
            
            # TECHNIQUE 4: Math operations for digit extraction.
            # Integer division by 10 gets the carry. (e.g., 18 // 10 = 1)
            carry = total // 10
            
            # Modulo 10 gets the actual digit to store in the current node. (e.g., 18 % 10 = 8)
            current.next = ListNode(total % 10)
            
            # Advance our result list pointer to the newly created node.
            current = current.next
            
            # Advance the pointers for l1 and l2, but only if they haven't reached the end yet.
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
        # Return the actual head of the resulting linked list, which is the node right 
        # after our initial placeholder dummy node.
        return dummy_head.next