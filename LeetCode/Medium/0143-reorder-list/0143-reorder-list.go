/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reorderList(head *ListNode)  {
    // Edge case: If the list is empty or has only one node, no reordering is needed
    if head == nil || head.Next == nil {
        return
    }
    
    // Step 1: Find the middle of the linked list
    slow, fast := head, head.Next
    for fast != nil && fast.Next != nil {
        slow = slow.Next
        fast = fast.Next.Next
    }
    
    // Step 2: Reverse the second half
    second := slow.Next
    slow.Next = nil // Split the list into two separate halves
    
    var prev *ListNode // In Go, pointers default to nil
    for second != nil {
        tmp := second.Next
        second.Next = prev
        prev = second
        second = tmp
    }
    
    // Step 3: Merge the two halves
    first := head
    second = prev // 'prev' is the head of the reversed half
    
    for second != nil {
        tmp1, tmp2 := first.Next, second.Next
        
        // Link nodes alternately
        first.Next = second
        second.Next = tmp1
        
        // Move pointers forward
        first = tmp1
        second = tmp2
    }
}