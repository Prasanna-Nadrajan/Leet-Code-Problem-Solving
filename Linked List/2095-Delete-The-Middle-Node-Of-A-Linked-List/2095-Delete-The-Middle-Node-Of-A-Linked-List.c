/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

typedef struct ListNode node;
struct ListNode* deleteMiddle(struct ListNode* head) {
    node* slow = head;
    node* fast = head;
    node* prev = NULL;
    while(fast && fast->next){
        prev=slow;
        slow=slow->next;
        fast=fast->next->next;
    }
    if(prev){
        prev->next=slow->next;
    }
    else{
        head=head->next;
    }
    return head;
}
