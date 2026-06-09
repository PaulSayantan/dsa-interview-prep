/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        // Base Case: Stop recursion when reaching the final node or an empty list
        if (head == nullptr || head->next == nullptr) {
            return head;
        }
        
        // Post-order traversal: Solve the sub-problem for all trailing nodes
        ListNode* new_head = reverseList(head->next);
        
        // Mutate pointers as the execution stack unwinds
        head->next->next = head;   // Force the next node to point back to us
        head->next = nullptr;      // Safely sever the forward link
        
        return new_head;           // Propagate the new head back to the caller
    }
};